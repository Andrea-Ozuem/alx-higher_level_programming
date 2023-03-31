#!/usr/bin/python3
'''sends a POST request to url json'''
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""
    res = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
    try:
        res = res.json()
        if len(res) == 0:
            print('No result')
        else:
            print("[{}] {}".format(res['id'], res['name']))
    except requests.exceptions.RequestException:
        print('Not a valid JSON')
