#!/usr/bin/python3
"""
a Python script that takes your GitHub credentials (username and
password) and uses the GitHub API to display your id
"""
import sys
from requests import get
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    headers = {
            "Accept": "application/vnd.github+json"
            }
    params = {
            "page": 1,
            "per_page": 10
            }
    url = "https://api.github.com/repos/{}/{}/commits".format(owner_name,
                                                              repo_name)
    response = get(url, params=params, headers=headers)
    try:
        user_datas = response.json()
        for user_data in user_datas:
            sha = user_data.get("sha")
            author_name = user_data.get("commit").get("author").get("name")
            print(sha + ":", author_name)
    except KeyError as f:
        print("None")
