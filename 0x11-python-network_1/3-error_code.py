#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL and
-- displays the body of the response decoded in utf-8.
-manage urllib.error.HTTPError exceptions
-- print: Error code: followed by the HTTP status code
"""


if __name__ == '__main__':
    from sys import argv
    from urllib.error import HTTPError
    from urllib.request import Request, urlopen

    url = argv[1]
    req = Request(url)
    try:
        with urlopen(req) as response:
            page = response.read()
            print(page.decode('utf-8'))
    except HTTPError as e:
        print('Error code: {}'.format(e.code))

