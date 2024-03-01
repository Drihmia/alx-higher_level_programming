#!/usr/bin/python3
"""
 a Python script that takes in a URL, sends a request to the URL and
 displays the body of the response (decoded in utf-8).
 I'll  manage urllib.error.HTTPError exceptions and print: Error code:
 followed by the HTTP status code.
"""
from urllib.request import urlopen
from urllib.error import HTTPError
from sys import argv


if __name__ == "__main__":
    if len(argv) == 2:
        url = argv[1]

        try:
            with urlopen(url) as response:
                print(response.read().decode('utf-8'))
        except HTTPError as f:
            print("Error code:", f.code)
