#!/bin/bash
# Sends a post request to the passed URL
curl -sX POST -d 'email=test@gmail.com' -d 'subject=I will always be here for PLD' "$1"
