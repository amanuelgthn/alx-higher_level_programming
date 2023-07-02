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
    url = 'https://api.github.com/users/octocat'
    response = requests.get(url, auth=(username, password))
    user_id = response.json().get("id")
    if user_id:
        print(user_id)