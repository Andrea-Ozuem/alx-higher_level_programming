#!/usr/bin/python3
'''sends a request to the URL displays the body of the response'''

if __name__ == "__main__":
    from urllib import request, error
    import sys

    try:
        with urllib.request.urlopen(sys.argv[1]) as res:
            content = res.read().decode('utf-8')
            print(content)
    except error.HTTPError as err:
        print('Error code: {}'.format(err.code))
