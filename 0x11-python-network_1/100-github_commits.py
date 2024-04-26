#!/usr/bin/python3
"""takes 2 arguments in order to solve this challenge."""

import sys
import requests

repo = sys.argv[1]
user = sys.argv[2]

url = "https://api.github.com/repos/{}/{}/commits".format(user, repo)

r = requests.get(url)

commits = r.json()

for commit in commits[:10]:
    sha = commit['sha']
    author = commit['commit']['author']['name']
    print("{}: {}".format(sha, author))