#!/usr/bin/python3
# 7-save_to_json_file.py
# Carlos Barros <1543@holbertonschool.com>
""" File name : 7-save_to_json_file.py
"""
import json


def save_to_json_file(my_obj, filename):
    """save_to_json_file writes an Object to a text file

    Args:
        my_obj (obj): any object for example list, dict
        filename: file name
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return(json.dump(my_obj, f))
