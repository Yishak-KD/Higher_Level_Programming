#!/usr/bin/python3
"""Error code"""

import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    try:
        req = requests.get(url)
        print(req.text)
    except requests.exceptions.HTTPError as e:
        print("Error code: {}".format(e))
