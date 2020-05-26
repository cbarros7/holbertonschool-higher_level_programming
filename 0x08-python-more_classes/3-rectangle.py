#!/usr/bin/python3
# 3-rectangle.py
# Carlos Barros <1543@holbertonschool.com>
""" File name : 3-rectangle.py
    String representation : print #
    It is not allowed to import any module
"""


class Rectangle(object):
    """Rectangle: Define new class"""
    def __init__(self, width=0, height=0):
        """ initializes the width and height """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ gets the width """
        return self.__width

    @width.setter
    def width(self, value):
        """ sets the width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ gets the height """
        return self.__height

    @height.setter
    def height(self, value):
        """ sets the height """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ method to find the area of a rectangle """
        return self.__height * self.__width

    def perimeter(self):
        """ method to find the perimeter of a rectangle """
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height * 2) + (self.__width * 2)

    def __str__(self):
        """ string representation of square """
        string = ""
        if self.__height == 0 or self.__width == 0:
            return string
        for y in range(self.__height):
            for x in range(self.__width):
                string += "#"
            string += "\n"
        string = string[:-1]
        return string
