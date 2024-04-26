#!/usr/bin/python3
""" Python script that fetches https://alx-intranet.hbtn.io/status"""

import urllib.requests
if __name__ == "__main__":
    with urllib.requests.urlopen("https://alx-intranet.hbtn.io/status") as res:
        status = res.read()

    print("Body response:")
    print(\n\t"- type: {}".format(type(status)))
    print(\n\t"- content: {}".format(status))
