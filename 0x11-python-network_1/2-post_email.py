#!/usr/bin/python3
'''sends a POST request to the URL with the email as a parameter'''

if __name__ == "__main__":
    import urllib.request
    from urllib.error import URLError, HTTPError
    import sys
    import urllib.parse

    val = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(val)
    data = data.encode('ascii')
    req = urllib.request.Request(sys.argv[1], data)
    try:
        with urllib.request.urlopen(req) as res:
            content = res.read().decode('utf-8')
            print(content)
    except URLError:
        pass
