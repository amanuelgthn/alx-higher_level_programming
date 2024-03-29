#!/usr/bin/python3
"""
Python script that takes in a letter and sends POST request to
        http://0.0.0.0:5000/search_user
- The letter must be sent in the variable q
- If no argument given set q=""
- if response if properly JSON formatted and not empty display the id and name
-- [<id>] <name>
-- Display Not a valid JSON if the JSON is invalid
-- Display No result if the JSON id empty
"""


if __name__ == "__main__":
    from sys import argv
    import requests

    url = 'http://0.0.0.0:5000/search_user'
    if len(argv) > 1:
        q = {'q': argv[1]}
    else:
        q = {'q': ''}
    request = requests.post(url, data=q)
    try:
        json_dict = request.json()
        if json_dict == {}:
            print('No result')
        else:
            print('[{}] {}'.format(json_dict['id'], json_dict['name']))
    except Exception:
        print('Not a valid JSON')
