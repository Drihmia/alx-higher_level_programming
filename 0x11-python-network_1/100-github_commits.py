#!/usr/bin/python3
"""
list 10 commits (from the most recent to oldest) of the repository “rails”
by the user  “rails”
You must use the GitHub API, here is the documentation
https://developer.github.com/v3/repos/commits/
Format: `<sha>: <author name>`
"""
import sys
from requests import get


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
