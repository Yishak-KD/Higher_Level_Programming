#!/usr/bin/env python3
# Fetch url using python script

import urllib.request
with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    html = response.read()
