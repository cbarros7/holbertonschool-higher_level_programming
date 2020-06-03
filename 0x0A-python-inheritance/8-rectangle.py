#!/usr/bin/python3
# 8-rectangle.py
# Carlos Barros <1543@holbertonschool.com>
""" File name : 8-rectangle.py
    It is not allowed to import any module
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Define class rectangle"""
    def __init__(self, width, height):
        """ instantiation 
        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
        """
        self.integer_validator = (("width", width))
        self.__width = width
        self.integer_validator = (("height", height))
        self.__height = height
