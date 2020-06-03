#!/usr/bin/python3
# 7-base_geometry.py
# Carlos Barros <1543@holbertonschool.com>
""" File name : 7-base_geometry.py
    It is not allowed to import any module
"""


class BaseGeometry:
    """Class BaseGeometry"""
    def area(self):
        """Raises an Exception - method not implemented"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates a given value is a positive int
        Param:
            name: name of variable to validate
            value: value to validate
        Raises:
            TypeError: if value is not an int
            ValueError: if value is negative
        """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0". format(name))
