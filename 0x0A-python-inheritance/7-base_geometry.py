#!/usr/bin/python3
# 7-base_geometry.py
# Carlos Barros <1543@holbertonschool.com>
""" File name : 7-base_geometry.py
    It is not allowed to import any module
"""


class BaseGeometry(object):
    """Define class base geometry"""
    def area(self):
        """area: return area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value"""
        self.name = name
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(self.name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(self.name))
