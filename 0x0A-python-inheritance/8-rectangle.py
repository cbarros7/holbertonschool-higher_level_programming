#!/usr/bin/python3
# 8-rectangle.py
# Carlos Barros <1543@holbertonschool.com>
""" File name : 8-rectangle.py
    It is not allowed to import any module
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Class Rectangle that inherits
    from class 'BaseGeometry'
    Attributes:
    ----------
    width  {int} -- [Rectangle's width]
    height {int} -- [Rectangle's height]
    """

    def __init__(self, width, height):
        """
        private attributes width and height,
        and validating if they are ints.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
