#!/usr/bin/python3
"""
Script that takes a URL, display the body of the response.

Usage: ./3-error_code.py <URL>
  - Handles HTTP errors.
"""

import urllib.request
import urllib.error
import sys

req = urllib.request.Request(sys.argv[1])
try:
    with urllib.request.urlopen(req) as resp:
        print(resp.read().decode("utf-8"))
except urllib.error.HTTPError as e:
    print("Error code: {}".format(e.code))
