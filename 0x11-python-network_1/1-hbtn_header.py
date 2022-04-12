#!/usr/bin/python3
# Python script that takes in a URL,
# Sends a request to the URL,
# Display the value of X-Request-Id

import urllib.request
import sys

if __name__ == '__main__':
    req = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(req) as response:
        print(response.headers.get('X-Request-Id'))
