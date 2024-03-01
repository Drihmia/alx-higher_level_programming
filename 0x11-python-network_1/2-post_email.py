#!/usr/bin/python3
"""
a Python script that takes in a URL and an email, sends a POST request to
the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8).
"""
from urllib.request import urlopen, Request
from urllib.parse import urlencode
from sys import argv


if __name__ == "__main__":
    if len(argv) == 3:
        url = argv[1]
        email = argv[2]
        values = {'email': email}

        data = urlencode(values)
        data_encoded = data.encode('ascii')
        request_object = Request(url, data_encoded)
        with urlopen(request_object) as response:
            print(response.read().decode('utf-8'))
