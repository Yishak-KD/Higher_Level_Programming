#!/bin/bash
# Script that sends request and displays only status code
curl -o /dev/null -sw "%{http_code}" "$1"
