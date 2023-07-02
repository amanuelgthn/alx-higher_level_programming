#!/usr/bin/python3
"""
Python script that takes GitHub credentials(username and password) and
uses the GitHub API to display your id
"""


if __name__ == '__main__':
    from sys import argv
    import requests
    from requests.auth import HTTPBasicAuth

    username = str(argv[1])
    password = str(argv[2])
    basic = (username, password)
    url = 'https://api.github.com/user'
    response = requests.get(url, auth=basic)
    try:
        user_id = response.json()['id']
        print(user_id)
    except KeyError:
        print('None')
