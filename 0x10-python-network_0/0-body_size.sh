#!/bin/bash
# A script that takes in a URL, and display size of body response
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
