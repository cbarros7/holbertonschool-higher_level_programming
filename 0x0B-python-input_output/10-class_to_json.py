#!/usr/bin/python3
# 10-class_to_json.py
# Carlos Barros <1543@holbertonschool.com>
""" File name : 10-class_to_json.py
"""
import json


def class_to_json(obj):
    """class_to_json return dictionary description with simple data structure

    Args:
        obj : any object for example list, dict
    """
    return(json.dumps(obj.__dict__))
