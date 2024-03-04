#!/usr/bin/python3
"""
a Python script that takes your GitHub credentials (username and
password) and uses the GitHub API to display your id
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    url = "https://api.github.com/{}".format("user")
    response = requests.get(url, auth=HTTPBasicAuth(username, password))
    try:
        user_data = response.json()
        user_id = user_data.get('id', None)
        print(user_id)
    except KeyError as f:
        print("None")

    # 2nd method using the json method
    # text = response.json()
    # print(text.get('id', None))
