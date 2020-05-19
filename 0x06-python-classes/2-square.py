#!/usr/bin/python3
# 2-square.py
# Carlos Barros <1543@holbertonschool.com>
"""Size validation: """


class Square(object):
    """class variable size"""
    def __init__(self, size=0):
        """initialize size"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
