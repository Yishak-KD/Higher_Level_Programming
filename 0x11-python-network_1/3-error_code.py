#!/usr/bin/python3
"""
Script that takes a URL, display the body of the response.
"""

import urllib.request
import urllib.error
import sys

if __name__ == '__main__':
    req = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(req) as resp:
            print(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
