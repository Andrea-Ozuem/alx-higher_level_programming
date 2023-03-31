#!/usr/bin/python3
'''fetches https://alx-intranet.hbtn.io/status'''

if __name__ == "__main__":
    import urllib.request
    from urllib.error import URLError, HTTPError

    req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    try:
        with urllib.request.urlopen(req) as res:
            content = res.read()
            print("Body response:")
            print(f"\t- type: {type(content)}")
            print(f"\t- content: {content}")
            print(f"\t- utf8 content: {content.decode('utf-8')}")
    except URLError:
        pass
