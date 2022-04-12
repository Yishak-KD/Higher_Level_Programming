#!/usr/bin/python3
# Python script that takes in a URL, and displays result

import urllib.request
import sys

if __name__ == "__main__":
    req = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(req) as response:
        print(dict(response.headers).get('X-Request-Id'))
