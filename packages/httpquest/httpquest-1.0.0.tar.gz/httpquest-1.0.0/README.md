# httpquest

**httpquest** is an advanced HTTP request library for Python, offering:

- Error handling and exceptions.
- Proxy support.
- Easy-to-use API.

## Installation

You can install `httpquest` using pip:


```pip install httpquest```


## Usage

Here's an example of how to use `httpquest` to make a GET request:

```python
from httpquest import get

response = get('https://example.com')
print(response.text)
```

```python
from httpquest import Session

session = Session(timeout=30) 
response = session.get('https://example.com')
print(response.text)
```

For more detailed usage instructions and examples, refer to the [documentation](https://github.com/cxstles/httpquest).
