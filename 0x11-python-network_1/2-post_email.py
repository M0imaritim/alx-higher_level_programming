#!/usr/bin/python3
"""takes in a URL and an email, sends a POST request to the passed URL with the
email as a parameterr, and displays the body of the response (decoded in utf-8)
"""
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    e_data = urllib.parse.urlencode({'Your email is': email})
    e_data = e_data.encode('ascii')
    with urllib.request.urlopen(url, data=e_data) as response:
        page = response.read().decode('utf-8')
    print(page)
