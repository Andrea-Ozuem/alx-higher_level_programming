#!/usr/bin/python3
'''fetches heaser var using requests'''
import requests
import sys


if __name__ == "__main__":
    content = requests.get(sys.argv[1])
    content = content.headers
    print(content.get('X-Request-Id'))
