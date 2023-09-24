from collections.abc import Mapping, MutableMapping
from collections import OrderedDict
from urllib.parse import urlsplit
import socket
import brotli
import socks
import zlib
import gzip
import ssl

from .model import Response
from .exceptions import *

# Mapping of supported schemes to proxy types
scheme_to_proxy_type = {
    "http": socks.HTTP,
    "https": socks.HTTP,
    "socks": socks.SOCKS4,
    "socks5": socks.SOCKS5,
    "socks5h": socks.SOCKS5,
}

# Mapping of schemes to default ports
scheme_to_port = {"http": 80, "https": 443}

class CaseInsensitiveDict(MutableMapping):
    """
    A case-insensitive dictionary-like object.

    Implements all methods and operations of MutableMapping as well as dict's copy. Also provides lower_items.

    Args:
        data (dict, optional): Initial data to populate the dictionary.

    Attributes:
        _store (OrderedDict): Internal storage for key-value pairs.

    Example:
        >>> cid = CaseInsensitiveDict({'Accept': 'application/json'})
        >>> cid['accept'] == 'application/json'  # True
    """

    def __init__(self, data=None, **kwargs):
        self._store = OrderedDict()
        if data is None:
            data = {}
        self.update(data, **kwargs)

    def __setitem__(self, key, value):
        """
        Set a key-value pair in the dictionary.

        Args:
            key (str): The key to set.
            value (any): The value associated with the key.
        """
        self._store[key.lower()] = (key, value)

    def __getitem__(self, key):
        """
        Get the value associated with a key.

        Args:
            key (str): The key to retrieve.

        Returns:
            any: The value associated with the key.

        Raises:
            KeyError: If the key is not found.
        """
        return self._store[key.lower()][1]

    def __delitem__(self, key):
        """
        Delete a key-value pair from the dictionary.

        Args:
            key (str): The key to delete.

        Raises:
            KeyError: If the key is not found.
        """
        del self._store[key.lower()]

    def __iter__(self):
        """
        Iterate through the keys in the dictionary.

        Returns:
            iterator: An iterator for keys.

        Example:
            >>> cid = CaseInsensitiveDict({'Accept': 'application/json'})
            >>> list(cid) == ['Accept']  # True
        """
        return (casedkey for casedkey, mappedvalue in self._store.values())

    def __len__(self):
        """
        Get the number of key-value pairs in the dictionary.

        Returns:
            int: The number of key-value pairs.

        Example:
            >>> cid = CaseInsensitiveDict({'Accept': 'application/json'})
            >>> len(cid) == 1  # True
        """
        return len(self._store)

    def lower_items(self):
        """
        Get an iterator of key-value pairs with lowercase keys.

        Returns:
            iterator: An iterator of key-value pairs with lowercase keys.

        Example:
            >>> cid = CaseInsensitiveDict({'Accept': 'application/json'})
            >>> list(cid.lower_items()) == [('accept', 'application/json')]  # True
        """
        return ((lowerkey, keyval[1]) for (lowerkey, keyval) in self._store.items())

    def __eq__(self, other):
        """
        Compare the dictionary with another dictionary.

        Args:
            other (dict): The dictionary to compare with.

        Returns:
            bool: True if the dictionaries are equal, False otherwise.

        Example:
            >>> cid1 = CaseInsensitiveDict({'Accept': 'application/json'})
            >>> cid2 = CaseInsensitiveDict({'accept': 'application/json'})
            >>> cid1 == cid2  # True
        """
        if isinstance(other, Mapping):
            other = CaseInsensitiveDict(other)
        else:
            return NotImplemented
        # Compare insensitively
        return dict(self.lower_items()) == dict(other.lower_items())

    def copy(self):
        """
        Create a shallow copy of the dictionary.

        Returns:
            CaseInsensitiveDict: A shallow copy of the dictionary.

        Example:
            >>> cid1 = CaseInsensitiveDict({'Accept': 'application/json'})
            >>> cid2 = cid1.copy()
            >>> cid1 == cid2  # True
        """
        return CaseInsensitiveDict(self._store.values())

    def __repr__(self):
        """
        Get a string representation of the dictionary.

        Returns:
            str: A string representation of the dictionary.

        Example:
            >>> cid = CaseInsensitiveDict({'Accept': 'application/json'})
            >>> repr(cid) == "{'Accept': 'application/json'}"  # True
        """
        return str(dict(self.items()))


class Session:
    """
    A session for making HTTP requests.

    This class provides methods for making various HTTP requests such as GET, POST,
    and more. It also handles features like proxy support, timeouts, and SSL
    certificate verification.
    """

    def __init__(
        self,
        proxies=None,
        timeout=None,
        chunk_size=None,
        decode_content=None,
        verify=None,
    ):
        """
        Initialize an HTTP session.

        Args:
            proxies (dict, optional): A dictionary of proxy URLs for different schemes.
            timeout (float, optional): The timeout for HTTP requests in seconds.
            chunk_size (int, optional): The maximum chunk size for reading data.
            decode_content (bool, optional): Whether to decode content.
            verify (bool, optional): Whether to verify SSL certificates.
        """
        timeout = timeout if timeout is not None else 60
        chunk_size = chunk_size if chunk_size is not None else (1024 ** 2)
        decode_content = decode_content if decode_content is not None else True
        verify = verify if verify is not None else True
        if proxies is None:
            proxies = {}
        else:
            for scheme, proxy_url in proxies.items():
                proxy = urlsplit(proxy_url)

                if scheme not in scheme_to_port:
                    raise UnsupportedScheme(
                        "'%s' is not a supported scheme" % (scheme)
                    )

                if proxy.scheme not in scheme_to_proxy_type:
                    raise UnsupportedScheme(
                        "'%s' is not a supported proxy scheme" % (proxy.scheme)
                    )

                proxies[scheme] = proxy

        self.timeout = timeout
        self.max_chunk_size = chunk_size
        self.decode_content = decode_content
        self.verify = verify
        self._scheme_to_proxy = proxies
        self._addr_to_conn = {}
        self._verified_context = ssl.create_default_context()

    def __enter__(self):
        """Enter the session context."""
        return self

    def __exit__(self, *_):
        """Exit the session context."""
        self.clear()

    def clear(self):
        """Clear session data and close connections."""
        addrs = list(self._addr_to_conn)
        while addrs:
            addr = addrs.pop()
            sock = self._addr_to_conn[addr]
            try:
                sock.shutdown(socket.SHUT_RDWR)
            except OSError:
                pass
            sock.close()
            self._addr_to_conn.pop(addr, None)

    def request(
        self,
        method,
        url,
        headers=None,
        data=None,
        timeout=None,
        verify=None,
        ciphers=None,
        version=None,
    ):
        """
        Make an HTTP request.

        Args:
            method (str): The HTTP method (e.g., GET, POST).
            url (str): The URL to request.
            headers (CaseInsensitiveDict, optional): The HTTP headers to include in the request.
            data (bytes or str, optional): The request body data.
            timeout (float, optional): The request timeout in seconds.
            verify (bool, optional): Whether to verify SSL certificates.
            ciphers (str, optional): A string specifying SSL ciphers.
            version (str, optional): The HTTP version to use (default is "1.1").

        Returns:
            Response: The HTTP response object.
        """
        parsed_url = urlsplit(url)
        if parsed_url.scheme not in scheme_to_port:
            raise UnsupportedScheme("'%s' is not a supported scheme" % (scheme))

        if verify is None:
            verify = self.verify

        if version is None:
            version = "1.1"

        if not isinstance(headers, CaseInsensitiveDict):
            headers = CaseInsensitiveDict(headers)

        if not "Host" in headers:
            headers["Host"] = parsed_url.hostname

        if data is not None:
            if not isinstance(data, bytes):
                data = data.encode("utf-8")

            if "Content-Length" not in headers:
                headers["Content-Length"] = int(len(data))

        host_addr = (
            parsed_url.hostname.lower(),
            parsed_url.port or scheme_to_port[parsed_url.scheme],
        )
        conn_reused = host_addr in self._addr_to_conn
        request = self._prepare_request(
            method=method,
            path=(
                parsed_url.path + ("?" + parsed_url.query if parsed_url.query else "")
            )
            or "/",
            version=version,
            headers=headers,
            body=data,
        )

        while True:
            try:
                conn = self._addr_to_conn.get(host_addr)
                if conn is None:
                    conn = self._create_socket(
                        host_addr,
                        proxy=self._scheme_to_proxy.get(parsed_url.scheme),
                        timeout=timeout if timeout is not None else self.timeout,
                        ssl_wrap=("https" == parsed_url.scheme),
                        ssl_verify=verify,
                        ciphers=ciphers,
                    )
                    self._addr_to_conn[host_addr] = conn
                else:
                    if timeout is not None:
                        conn.settimeout(timeout)

                conn.send(request)
                return self._get_response(
                    conn, self.max_chunk_size, self.decode_content
                )

            except Exception as err:
                if host_addr in self._addr_to_conn:
                    self._addr_to_conn.pop(host_addr)

                if not conn_reused:
                    if not isinstance(err, RequestException):
                        err = RequestException(err)
                    raise err

                conn_reused = False

    def get(self, url, **kwargs):
        """
        Make a GET request.

        Args:
            url (str): The URL to request.
            **kwargs: Additional keyword arguments to pass to the request method.

        Returns:
            Response: The HTTP response object.
        """
        return self.request("GET", url, **kwargs)

    def post(self, url, **kwargs):
        """
        Make a POST request.

        Args:
            url (str): The URL to request.
            **kwargs: Additional keyword arguments to pass to the request method.

        Returns:
            Response: The HTTP response object.
        """
        return self.request("POST", url, **kwargs)

    def options(self, url, **kwargs):
        """
        Make an OPTIONS request.

        Args:
            url (str): The URL to request.
            **kwargs: Additional keyword arguments to pass to the request method.

        Returns:
            Response: The HTTP response object.
        """
        return self.request("OPTIONS", url, **kwargs)

    def head(self, url, **kwargs):
        """
        Make a HEAD request.

        Args:
            url (str): The URL to request.
            **kwargs: Additional keyword arguments to pass to the request method.

        Returns:
            Response: The HTTP response object.
        """
        return self.request("HEAD", url, **kwargs)

    def put(self, url, **kwargs):
        """
        Make a PUT request.

        Args:
            url (str): The URL to request.
            **kwargs: Additional keyword arguments to pass to the request method.

        Returns:
            Response: The HTTP response object.
        """
        return self.request("PUT", url, **kwargs)

    def patch(self, url, **kwargs):
        """
        Make a PATCH request.

        Args:
            url (str): The URL to request.
            **kwargs: Additional keyword arguments to pass to the request method.

        Returns:
            Response: The HTTP response object.
        """
        return self.request("PATCH", url, **kwargs)

    def delete(self, url, **kwargs):
        """
        Make a DELETE request.

        Args:
            url (str): The URL to request.
            **kwargs: Additional keyword arguments to pass to the request method.

        Returns:
            Response: The HTTP response object.
        """
        return self.request("DELETE", url, **kwargs)

    @staticmethod
    def _create_socket(
        dest_addr,
        proxy=None,
        timeout=None,
        ssl_wrap=True,
        ssl_verify=True,
        remote_dns=False,
        ciphers=None,
    ):
        """
        Create a socket for the given destination address.

        Args:
            dest_addr (tuple): A tuple containing the destination address (hostname, port).
            proxy (urlsplit, optional): The proxy URL to use.
            timeout (float, optional): The socket timeout in seconds.
            ssl_wrap (bool, optional): Whether to wrap the socket with SSL.
            ssl_verify (bool, optional): Whether to verify SSL certificates.
            remote_dns (bool, optional): Whether to resolve DNS remotely (for SOCKS).
            ciphers (str, optional): A string specifying SSL ciphers.

        Returns:
            socket.socket: A socket object.
        """
        if proxy is None:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            sock = socks.socksocket()
            sock.set_proxy(
                scheme_to_proxy_type[proxy.scheme],
                addr=proxy.hostname,
                port=proxy.port,
                username=proxy.username,
                password=proxy.password,
                rdns=remote_dns,
            )

        if timeout:
            sock.settimeout(timeout)

        sock.connect(dest_addr)

        if ssl_wrap:
            context = (
                ssl.create_default_context() if ssl_verify else ssl.SSLContext()
            )
            if ciphers is not None:
                context.set_ciphers(ciphers)
            sock = context.wrap_socket(sock, server_hostname=dest_addr[0])

        return sock

    @staticmethod
    def _prepare_request(method, path, version, headers, body):
        """
        Prepare an HTTP request.

        Args:
            method (str): The HTTP method.
            path (str): The request path.
            version (str): The HTTP version.
            headers (CaseInsensitiveDict): The HTTP headers.
            body (bytes): The request body.

        Returns:
            bytes: The prepared HTTP request as bytes.
        """
        request = "%s %s HTTP/%s\r\n" % (method, path, version)

        for header, value in headers.items():
            if value is None:
                continue
            request += "%s: %s\r\n" % (header, value)

        request += "\r\n"
        request = request.encode("UTF-8")

        if body is not None:
            request += body

        return request

    @staticmethod
    def _get_response(conn, max_chunk_size, decode_content):
        """
        Get an HTTP response.

        Args:
            conn (socket.socket): The socket connection.
            max_chunk_size (int): The maximum chunk size for reading data.
            decode_content (bool): Whether to decode content.

        Returns:
            Response: The HTTP response object.
        """
        resp = conn.recv(max_chunk_size)

        if len(resp) == 0:
            raise EmptyResponse("Empty response from server")

        resp, data = resp.split(b"\r\n\r\n", 1)
        resp = resp.decode()
        status, raw_headers = resp.split("\r\n", 1)
        version, status, message = status.split(" ", 2)

        headers = CaseInsensitiveDict()
        for header in raw_headers.splitlines():
            header, value = header.split(":", 1)
            value = value.lstrip(" ")
            if header in headers:
                if isinstance(headers[header], str):
                    headers[header] = [headers[header]]
                headers[header].append(value)
            else:
                headers[header] = value

        if "content-length" in headers:
            goal = int(headers["content-length"])
            while goal > len(data):
                chunk = conn.recv(min(goal - len(data), max_chunk_size))
                if len(chunk) == 0:
                    raise RequestException("Empty chunk")
                data += chunk

        elif headers.get("transfer-encoding") == "chunked":
            while True:
                chunk = conn.recv(max_chunk_size)
                if len(chunk) == 0 or chunk == b"0\r\n\r\n":
                    break
                data += chunk

            raw = data
            data = b""
            while raw:
                length, raw = raw.split(b"\r\n", 1)
                length = int(length, 16)
                chunk, raw = raw[:length], raw[length + 2 :]
                data += chunk

        else:
            while True:
                chunk = conn.recv(max_chunk_size)
                if len(chunk) == 0:
                    break
                data += chunk

        if "content-encoding" in headers:
            # Handle content encoding like gzip, deflate, etc.
            if headers["content-encoding"].lower() == "gzip":
                data = gzip.decompress(data)
            elif headers["content-encoding"].lower() == "deflate":
                data = zlib.decompress(data)
            elif headers["content-encoding"].lower() == "br":
                data = brotli.decompress(data)

        return Response(
            status_code=int(status),
            headers=headers,
            content=data,
            message=message,
        )

    def close(self):
        """
        Close the session and its connections.

        This method closes all open socket connections and clears internal state.
        """
        self.clear()

