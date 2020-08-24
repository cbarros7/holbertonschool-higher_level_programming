#!/usr/bin/python3
"""Error code #0"""
import requests

if __name__ == "__main__":
    response = requests.get('https://intranet.hbtn.io/status')
    req = "Body response:\n\t- type: {}\n\t- content: {}"
    print(req.format(type(response.text), response.text))
