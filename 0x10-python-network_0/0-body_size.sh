#!/bin/bash
# Script that displays size of the body of the response

curl -sI "$1" | grep -i Content-Length
