#!/usr/bin/python3
# 101-locked_class.py
# Carlos Barros <1543@holbertonschool.com>
""" File name : 101-locked_class.py
    Low memory cost: Defines a locked class
    It is not allowed to import any module
"""


class LockedClass:
    """
    Prevent the user from instantiating new LockedClass attributes
    for anything but attributes called 'first_name'.
    """

    __slots__ = ["first_name"]
