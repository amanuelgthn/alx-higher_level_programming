#!/usr/bin/python3
"""
Python script that takes in a url sends a request to the URL and
displays the value of the variable X-Request_Id in the response header
"""


if __name__ == '__main__':
    import requests
    from sys import argv

    url = argv[1]
    try:
        response = requests.get(url)
        print(response.headers['X-Request-Id'])
    except KeyError:
        pass
