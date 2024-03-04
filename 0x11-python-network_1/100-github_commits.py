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
        commits = response.json()
        for commit in commits:
            sha = commit.get("sha")
            n = "name"
            author_name = commit.get("commit", {}).get("author", {}).get(n)
            print("{}: {}".format(sha, author_name))
    except (KeyError, AttributeError) as f:
        print("None")
