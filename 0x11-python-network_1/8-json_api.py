#!/usr/bin/python3
"""
takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter
"""
import sys
import requests

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    let = sys.argv[1] if len(sys.argv) > 1 else ""
    e_data = {'q': let}
    r = requests.post(url, data=e_data)
    try:
        rc = r.json()
        if rc:
            print("[{}] {}".format(rc.get("id"), rc.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
