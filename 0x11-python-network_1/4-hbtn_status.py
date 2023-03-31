#!/usr/bin/python3
'''fetches url using requests'''
import requests


if __name__ == "__main__":
    content = requests.get('https://alx-intranet.hbtn.io/status')
    content = content.text
    print("Body response:")
    print(f"\t- type: {type(content)}")
    print(f"\t- content: {content}")
