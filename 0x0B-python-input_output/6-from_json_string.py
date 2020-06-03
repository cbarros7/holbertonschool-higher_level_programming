#!/usr/bin/python3
# 6-from_json_string.py
# Carlos Barros <1543@holbertonschool.com>
""" File name : 6-from_json_string.py
"""
import json


def from_json_string(my_str):
    """from_json_string  returns an object
    (Python data structure) represented by a JSON string

    Args:
        my_str (obj): any object for example list, dict
    """
    return(json.loads(my_str))
