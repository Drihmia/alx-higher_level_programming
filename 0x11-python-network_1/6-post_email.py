#!/usr/bin/python3
"""
a Python script that takes in a 'URL' and an 'email address', sends a POST
request to the passed URL with the email as a parameter, and
finally displays the body of the response.

The email will be sent in the variable email
"""
from requests import post
from sys import argv


if __name__ == "__main__":
    if len(argv) == 3:
        url = argv[1]
        email = argv[2]
        payload = {"email": email}

        response = post(url, data=payload)
        print(response.text)
