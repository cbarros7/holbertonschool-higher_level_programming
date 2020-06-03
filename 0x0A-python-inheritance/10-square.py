#!/usr/bin/python3
# 10-square.py
# Carlos Barros <1543@holbertonschool.com>
""" File name : 10-square.py
    It is not allowed to import any module
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square -- Multiple inheritance"""
    def __init__(self, size):
        self.integer_validator = (("my_int", size))
        super().__init__(size, size)
        self.__size = size