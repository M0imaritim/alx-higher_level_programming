#!/usr/bin/python3
"""
    Python script that takes in a URL, sends a request to the URL and displays
    the body of the response
"""
import sys
import urllib.request

url = sys.argv[1]
try:
    with urllib.request.urlopen(url) as response:
        result = response.read()
        print(result)
except urllib.error.HTTPError as e:
    print("Error code: {}".format(e))
