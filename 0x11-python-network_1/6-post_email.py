#!/usr/bin/python3
"""Response header value"""
import requests
import sys

if __name__ == "__main__":
    email = sys.argv[2]
    req = requests.post(sys.argv[1], data={'email': email})
    print(req.text)
