#!/usr/bin/python3
"""Response header value"""
import urllib.request
import sys

with urllib.request.urlopen(sys.argv[1]) as url:
    s = url.getheader('X-Request-Id')
    print(s)
