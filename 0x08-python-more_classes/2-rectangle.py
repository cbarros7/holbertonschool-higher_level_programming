#!/usr/bin/python3
# 2-rectangle.py
# Carlos Barros <1543@holbertonschool.com>
""" File name : 2-rectangle.py
    Area and Perimeter : calculate area and perimeter
    It is not allowed to import any module
"""


class Rectangle(object):
    """Rectangle: Define new class"""
    def __init__(self, width=0, height=0):
        """Initialize new class rectangle

        Args:
            width (int): width for the new rectangle
            height (int): height for the new rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Property for attribute width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set values to width

        Args:
            value (int): new value for width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Property for attribute height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set values to height

        Args:
            value (int): new value for height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Define area"""
        return self.__width * self.__height

    def perimeter(self):
        """Define perimeter"""
        if (self.width or self.height) != 0:
            return ((2 * self.__width) + (2 * self.__height))
        return 0
