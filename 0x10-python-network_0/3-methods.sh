#!/bin/bash
# Display all HTTP methods server will accept
curl -si -X OPTIONS "$1"
