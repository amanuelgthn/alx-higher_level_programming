#!/usr/bin/python3
"""
Python script that takes 2 arguments in order to list last 10 commits
-- first argument repository name
-- second argument owner name
"""


if __name__ == '__main__':
    import requests
    from sys import argv

    repo_name = argv[1]
    owner_name = argv[2]
    url = 'https://api.github.com/repos'
    refined_url = '{}/{}/{}/commits'.format(url, owner_name, repo_name)
    response = requests.get(refined_url)
    json_response = response.json()
    for i in range(len(json_response)):
        if i < 10:
            commits = json_response[i]
            print('{}: {}'.format(commits['sha'],
                                  commits['commit']['author']['name']))
