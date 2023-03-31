#!/usr/bin/python3
'''sends a POST request to url and email data'''
import requests
import sys


if __name__ == "__main__":
    content = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(content.text)
