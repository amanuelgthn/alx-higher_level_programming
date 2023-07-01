#!/usr/bin/python3
"""
Python script that takes in a URL and an email,sends a POST request
displays the body of the response
-email sent in email variable
"""


if __name__ == "__main__":
    import sys
    from urllib.parse import urlencode
    from urllib.request import Request
    from urllib.request import urlopen

    url = sys.argv[1]
    email = {'email': str(sys.argv[2])}
    data = urlencode(email)
    url_ful = url + '?' + data
    with urlopen(url_ful) as response:
        page = response.read()
        print(page.decode('utf-8'))
