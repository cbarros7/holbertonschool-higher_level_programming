#!/usr/bin/python3
# 9-rectangle.py
# Carlos Barros <1543@holbertonschool.com>
""" File name : 9-rectangle.py
    It is not allowed to import any module
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Define class rectangle
    """
    def __init__(self, width, height):
        """
        instantiation
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        Define are recantgle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        print string
        """
        return '[Rectangle] {}/{}'.format(self.__width, self.__height)
