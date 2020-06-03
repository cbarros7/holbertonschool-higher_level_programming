#!/usr/bin/python3
# 11-square.py
# Carlos Barros <1543@holbertonschool.com>
""" File name : 11-square.py
    It is not allowed to import any module
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square -- Multiple inheritance"""
    def __init__(self, size):
        """Initialize a new square.
        Args:
            size (int): The size of the new square.
        """
        self.integer_validator("my_int", size)
        super().__init__(size, size)
        self.size = size

    def __str__(self):
        """print string"""
        return '[Square] {}/{}'.format(self.size, self.size)
