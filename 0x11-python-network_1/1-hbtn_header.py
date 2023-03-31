#!/usr/bin/python3
'''displays the value of the X-Request-Id variable found in the header of the response'''

if __name__ == "__main__":
    import urllib.request
    from urllib.error import URLError, HTTPError
    import sys

    req = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(req) as res:
            content = res.headers
            print(content.get('X-Request-Id'))
    except URLError:
        pass
