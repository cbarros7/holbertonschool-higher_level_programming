#!/usr/bin/python3
# 4-inherits_from.py
# Carlos Barros <1543@holbertonschool.com>
""" File name : 4-inherits_from.py
    It is not allowed to import any module
"""


def inherits_from(obj, a_class):
    """inherits_from: returns True if the
    object is an instance of a class that inherited
    (directly or indirectly) from the specified class ;
    otherwise False.

    Args:
        obj: object
        a_class: class
    """
    if type(obj) != a_class and issubclass(type(obj), a_class):
        return True
    return False
