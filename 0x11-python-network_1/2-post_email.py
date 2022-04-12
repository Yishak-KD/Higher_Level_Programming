#!/usr/bin/python3
"""
Script that takes in a URL and an email, sends POST request
"""

import urllib.request
import urllib.parse
import sys

if __name__ == '__main__':
    value = {"Email": sys.argv[2]}

    data = urllib.parse.urlencode(value).encode('ascii')

    req = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
