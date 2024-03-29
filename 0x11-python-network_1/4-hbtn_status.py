#!/usr/bin/python3
"""
Python script that fetches https://alx-intranet.hbtn.io/status
"""


if __name__ == '__main__':
    import requests

    url = 'https://alx-intranet.hbtn.io/status'
    response = requests.get(url)
    page = response.text
    print("Body response:")
    print('\t- type: {}'.format(type(page)))
    print('\t- content: {}'.format(page))
