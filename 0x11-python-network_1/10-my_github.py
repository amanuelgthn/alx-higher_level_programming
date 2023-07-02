#!/usr/bin/python3
"""
Python script that takes GitHub credentials(username and password) and
uses the GitHub API to display your id
"""


if __name__ == '__main__':
    from sys import argv
    import requests

    username = argv[1]
    password = argv[2]
    url = 'https://api.github.com'
    response = requests.get(url, auth=(username, password))
    user_id = response.json()
    try:
        print(user_id['id'])
    except Exception:
        print('None')
