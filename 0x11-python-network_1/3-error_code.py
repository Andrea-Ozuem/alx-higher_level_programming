#!/usr/bin/python3
'''displays the body of the response'''

if __name__ == "__main__":
    import urllib.request
    import sys

    req = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(req) as res:
            content = res.read().decode('utf-8')
            print(content)
    except urllib.error.HTTPError as err:
        print('Error code: {}'.format(err.code))
