#!/usr/bin/python3
'''sends a github using github api'''
import requests
import sys


if __name__ == "__main__":
    url = 'https://api.github.com/repos/{}/{}/commits'.format(sys.argv[2],
                                                              sys.argv[1])
    headers = {'X-GitHub-Api-Version': '2022-11-28',
               'Accept': 'application/vnd.github+json'}
    res = requests.get(url, headers=headers)
    try:
        res = res.json()
        for i in range(10):
            print('{}: {}'.format(res[i].get('sha'), res[i].get('commit')
                  .get('author').get('name')))
    except ValueError:
        pass
