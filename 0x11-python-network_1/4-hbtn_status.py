#!/usr/bin/python3
# Python script that fetches information
import requests

if __name__ == "__main__":
    r = requests.get('https://alx-intranet.hbtn.io/status')

    print("Body response:")
    print(f"\t- type: {type(str(r))}")
    print(f"\t- content: {r.text}")
