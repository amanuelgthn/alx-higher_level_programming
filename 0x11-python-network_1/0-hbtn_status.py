#!/usr/bin/python3
"""
-Python script tha fetches https://alx-intranet.hbtn.io/status
-using urllib
-body of the response must be displayed (tabulation before -)
"""


if __name__ == '__main__':
    from urllib.request import Request, urlopen

    url = "https://alx-intranet.hbtn.io/status"
    request = Request(url)
    with urlopen(request) as response:
        page = response.read()
        print("Body response:")
        print('\t- type: {}'.format(type(page)))
        print('\t- content: {}'.format(page))
        print('\t- utf8 content: {}'.format(page.decode('utf8')))
