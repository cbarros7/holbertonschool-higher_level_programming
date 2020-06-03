#!/usr/bin/python3
# 2-is_same_class.py
# Carlos Barros <1543@holbertonschool.com>
""" File name : 2-is_same_class.py
    It is not allowed to import any module
"""


def is_same_class(obj, a_class):
    """Define if a obj is instance of class"""
    if type(obj) == a_class:
        return True
    return False
