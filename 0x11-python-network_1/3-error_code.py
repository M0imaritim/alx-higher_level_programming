#!/usr/bin/python3
"""
    Python script that takes in a URL, sends a request to the URL and displays
    the body of the response
"""
import sys
from urllib import request, error


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with request.urlopen(url) as response:
            result = response.read().decode('utf-8')
            print(result)
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
