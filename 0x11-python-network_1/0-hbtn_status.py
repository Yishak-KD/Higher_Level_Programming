#!/usr/bin/python3
"""
using urllib package that fetches
"""
import urllib.request

if __name__ == '__main__':
    request = urllib.request.Request("https://intranet.hbtn.io/status")
    with urllib.request.urlopen(request) as response:
        resp = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(resp)))
        print("\t- content: {}".format(resp))
        print("\t- utf8 content: {}".format(resp.decode('utf-8')))
