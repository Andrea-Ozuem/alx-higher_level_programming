#!/usr/bin/python3
'''sends a request to url get status code'''
import requests
import sys


if __name__ == "__main__":
    res = requests.get(sys.argv[1])
    if res.status_code >= 400:
        print('Error code: {}'.format(res.status_code))
    else:
        print(res.text)
