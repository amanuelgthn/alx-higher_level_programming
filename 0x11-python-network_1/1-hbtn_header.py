#!/usr/bin/python3
"""
- python script that takes in a URL, sends a request to the URL and
-- displays the value of
- the X-Request-Id variable found in the header response
"""


if __name__ == "__main__":
    import sys
    from urllib.request import Request
    from urllib.request import urlopen

    url = sys.argv[1]
    req = Request(url)
    with urlopen(req) as response:
        header = response.info()
        print(header['X-Request-Id'])
