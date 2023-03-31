#!/usr/bin/python3
'''sends a github using github api'''
import requests
import sys


if __name__ == "__main__":
    url = 'https://api.github.com/users/{}'.format(sys.argv[1])
    headers = {'Authorization': f'Bearer {sys.argv[2]}',
               'X-GitHub-Api-Version': '2022-11-28',
               'Accept': 'application/vnd.github+json'}
    res = requests.get(url, headers=headers)
    try:
        res = res.json()
        print(res.get('id'))
    except ValueError:
        pass
