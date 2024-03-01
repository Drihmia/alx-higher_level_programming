#!/usr/bin/python3
"""a Python script that fetches https://alx-intranet.hbtn.io/status"""
from urllib.request import urlopen

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    with urlopen(url) as response:
        byte_content = response.read()
        print("Body response:")
        print("\t- type:", type(byte_content))
        print("\t- content:", byte_content)
        print("\t- utf8 content:", byte_content.decode())
