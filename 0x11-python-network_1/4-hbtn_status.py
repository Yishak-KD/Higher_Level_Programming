#!/usr/bin/python3
"""Script that fetches with requests package"""

import requests
req = requests.get('https://alx-intranet.hbtn.io/status')
print("Body response:")
print("\t- type: {}".format(type(req.text)))
print("\t- content: {}".format(req.content.decode('utf-8')))
