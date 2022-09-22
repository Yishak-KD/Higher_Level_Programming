#!/bin/bash
# A script that takes a URL and display all HTTP methods
curl -sI "$1" | grep -i Allow | cut -d\  -f2-
