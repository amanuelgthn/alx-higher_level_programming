#!/usr/bin/python3
"""
Python script that takes in a URL and an email address,
sends a POST request to the specified URL with the email and
displays the response
"""


if __name__ == '__main__':
    from sys import argv
    import requests

    email = {'email': argv[2]}
    url = argv[1]
    response = requests.post(url, data=email)
    print(response.text)
