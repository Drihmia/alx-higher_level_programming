#!/usr/bin/python3
"""
a Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.

The letter must be sent in the variable q
If no argument is given, set q=""
If the response body is properly JSON formatted and not empty, display
the id and name like this: [<id>] <name>
Otherwise:
    Display Not a valid JSON if the JSON is invalid
    Display No result if the JSON is empty
"""
from requests import post
from sys import argv


if __name__ == "__main__":
    argc = len(argv)

    if argc == 1:
        q = ""
    else:
        q = argv[1]

    url = 'http://0.0.0.0:5000/search_user'
    values = {"q": q}
    response = post(url, data=values)
    try:
        json_res = response.json()
        if not json_res:
            print("No result")
        else:
            print("[{}] {}".format(json_res["id"], json_res["name"]))
    except Exception as f:
        print("Not a valid JSON")
