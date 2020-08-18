#!/bin/bash
# cURL POST parameters
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
