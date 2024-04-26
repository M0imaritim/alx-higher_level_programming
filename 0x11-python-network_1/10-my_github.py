#!/usr/bin/python3
""" takes your GitHub credentials (username and password) and uses the GitHub
API to display your id"""

import sys
import requests

if __name__ == "__main__":
    user = sys.argv[1]
    psswd = sys.argv[2]
    url = "https://api.github.com/user"

    auth = (user, psswd)

    r = requests.get(url, auth=auth)

    user_data = r.json()
    print(user_data['id'])
