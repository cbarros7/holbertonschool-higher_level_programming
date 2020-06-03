#!/usr/bin/python3
# 5-to_json_string.py
# Carlos Barros <1543@holbertonschool.com>
""" File name : 5-to_json_string.py
"""
import json


def to_json_string(my_obj):
    """to_json_string  returns the JSON representation of an object (string)

    Args:
        my_obj (obj): any object for example list, dict
    """
    return(json.dumps(my_obj))
