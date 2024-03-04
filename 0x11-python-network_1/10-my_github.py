#!/usr/bin/python3
"""
a Python script that takes your GitHub credentials (username and
password) and uses the GitHub API to display your id
"""
import sys
import requests


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    url = 'https://api.github.com/{}'.format("user")
    headers = {
            "Authorization": f"Bearer {password}",
            "Accept": "application/vnd.github.v3+json",
            "X-GitHub-Api-Version": "2022-11-28"
            }
    response = requests.get(url, auth=(username, password), headers=headers)
    try:
        # print("++++", response.request.headers)
        if response.status_code == 200:
            # for i, j in response.headers.items():
            # if i == "Vary":
            # for h in response.headers[i].split(","):
            # print(h)
            # print("- ", i, "   ", j)
            user_data = response.json()
            # print(user_data)
            user_id = user_data['id']
            print(user_id)
        else:
            print("None")
    except Exception as f:
        print("None")

    # 2nd method using the json method
    # text = response.json()
    # print(text.get('id', None))
