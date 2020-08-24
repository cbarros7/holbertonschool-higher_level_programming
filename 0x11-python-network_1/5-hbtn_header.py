#!/usr/bin/python3
"""Response header value"""
import requests
import sys

print("{}".format(requests.get(sys.argv[1]).headers['X-Request-Id']))
