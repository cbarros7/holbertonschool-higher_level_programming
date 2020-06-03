#!/usr/bin/python3
# 8-load_from_json_file.py
# Carlos Barros <1543@holbertonschool.com>
""" File name : 8-load_from_json_file.py
"""
import json


def load_from_json_file(filename):
    """ def load_from_json_file(filename): creates an Object from a JSON file

    Args:
        my_obj (obj): any object for example list, dict
        filename: file name
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return(json.load(f))
