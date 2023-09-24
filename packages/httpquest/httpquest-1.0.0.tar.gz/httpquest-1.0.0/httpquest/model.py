import json as jsonlib

class Response:
    def __init__(self, status_code, message, headers, content):
        """
        Initialize a Response object.

        Args:
            status_code (int): The HTTP status code.
            message (str): The status message.
            headers (dict): The response headers.
            content (bytes): The response content.
        """
        self.status_code = status_code
        self.message = message
        self.headers = headers
        self.content = content

    def __repr__(self):
        """
        Return a string representation of the Response object.
        """
        return f"<Response [{self.status_code}]>"

    def json(self):
        """
        Deserialize the response content as JSON.

        Returns:
            dict: The JSON-decoded content.
        """
        return jsonlib.loads(self.content)

    @property
    def text(self):
        """
        Get the response content as text.

        Returns:
            str: The response content as a text string.
        """
        return self.content.decode("UTF-8", errors="ignore")
