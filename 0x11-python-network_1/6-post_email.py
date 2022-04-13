#!/usr/bin/python3
"""
Script that takes a URL and sends a POST request
"""

import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    load = {'email': sys.argv[2]}
    r = requests.post(url, data=load)
    print(r.text)
