#!/usr/bin/python3
"""
a Python script that fetches https://alx-intranet.hbtn.io/status
I will use the package requests
"""
from requests import get


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    response = get(url)
    print("Body response:")
    print("\t- type:", type(response.text))
    print("\t- content:", response.text)
