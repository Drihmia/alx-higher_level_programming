#!/usr/bin/python3
"""
a Python script that takes in a URL, sends a request to the URL
and displays the value of the variable X-Request-Id in the response header
"""
from requests import get
from sys import argv


if __name__ == "__main__":
    if len(argv) == 2:
        url = argv[1]

        response = get(url)
        print(response.headers.get('X-Request-Id'))
