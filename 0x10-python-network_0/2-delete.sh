#!/bin/bash
# A script that sends a Delete request to URL passed as first argument
curl -sX "DELETE" "$1"
