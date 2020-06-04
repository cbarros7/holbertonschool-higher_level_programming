#!/usr/bin/python3
# 10-class_to_json.py
# Carlos Barros <1543@holbertonschool.com>
""" File name : 10-class_to_json.py
"""


def class_to_json(obj):
    """class_to_json return dictionary description with simple data structure

    Args:
        obj : any object for example list, dict
    """
    return obj.__dict__
