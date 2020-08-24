#!/usr/bin/python3
"""Search API """
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        a_dict = {'q': ''}
    elif len(sys.argv) > 1:
        a_dict = {'q': sys.argv[1]}

    try:
        req = requests.post('http://0.0.0.0:5000/search_user', a_dict)
        if req.json():
            print('[{}] {}'.format(req.json().get('id'),
                                   req.json().get('name')))
        else:
            print('No result')

    except ValueError:
        print("Not a valid JSON")
