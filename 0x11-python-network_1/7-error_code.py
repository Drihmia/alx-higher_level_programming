#!/usr/bin/python3
"""
a Python script that takes in a URL, sends a request to the URL and
displays the body of the response.

If the HTTP status code is greater than or equal to 400, print: Error code:
followed by the value of the HTTP status code
"""
from requests import get
from sys import argv


if __name__ == "__main__":
    if len(argv) == 2:
        url = argv[1]

        response = get(url)
        status_code = response.status_code

        if status_code >= 400:
            print("Error code:", status_code)
        else:
            print(response.text)
