#!/usr/bin/python3
'''fetches https://alx-intranet.hbtn.io/status'''
from urllib.error import URLError, HTTPError
import urllib.request

req = urllib.request.Request('http://www.voidspace.org.uk')
try:
    with urllib.request.urlopen(req) as response:
        the_page = response.read()
except HTTPError as e:
    print('Error code: ', e.code)
except URLError as e:
    print('We failed to reach a server.')
    print('Reason: ', e.reason)
