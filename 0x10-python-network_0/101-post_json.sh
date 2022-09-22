#!/bin/bash
# Script that sends JSON POST request to URL passed as first argument
curl -sX POST -H "Content-type: application/json" -H "Accept: application/json" -d "@$2" "$1"
