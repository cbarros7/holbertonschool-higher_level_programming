#!/usr/bin/python3
"""Response header value"""
import requests
import sys

if __name__ == "__main__":
    print("{}".format(requests.get(sys.argv[1]).headers.get('X-Request-Id')))
