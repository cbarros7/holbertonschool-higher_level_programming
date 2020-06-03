#!/usr/bin/python3
# 7-base_geometry.py
# Carlos Barros <1543@holbertonschool.com>
"""Represent BaseGeometry class
"""


class BaseGeometry:
    """Represent BaseGeometry"""
    def area(self):
        """Represent area
        Raises:
            Exception: [area() is not implemented]
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value
        Arguments:
            name {str} -- name of an instance
            value {int} -- type of instance
        Raises:
            TypeError: [must be an integer]
            ValueError: [must be greater than 0]
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
