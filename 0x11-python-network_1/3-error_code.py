#!/usr/bin/python3
'''displays the body of the response'''

if __name__ == "__main__":
    import urllib.request
    from urllib.error import URLError, HTTPError
    import sys

    req = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(req) as res:
            content = res.read().decode('utf-8')
            print(content)
    except HTTPError as e:
        print('Error code: {}'.format(e.code))
