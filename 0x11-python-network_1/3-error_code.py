#!/usr/bin/python3
'''sends a request to the URL displays the body of the response'''
from urllib import request, error
import sys


if __name__ == "__main__":
    try:
        with request.urlopen(sys.argv[1]) as res:
            content = res.read().decode('utf-8')
            print(content)
    except error.HTTPError as err:
        print('Error code: {}'.format(err.code))
