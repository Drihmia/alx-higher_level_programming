#!/usr/bin/python3
"""
a Python script that takes in a URL, sends a request to the URL and displays
the value of the 'X-Request-Id' variable found in the header of the response.
"""
from urllib.request import urlopen
from sys import argv


if __name__ == "__main__":
    if len(argv) == 2:
        url = argv[1]
        with urlopen(url) as response:
            # methode 1 : using getheader method in response object
            print(response.getheader("X-Request-Id"))

            # method 2: using dictionary and some manipulation
            # headers = response.__dict__.get("headers")
            # index_var = headers.keys().index('X-Request-Id')
            # print(response.__dict__.get("headers").values()[index_var])
