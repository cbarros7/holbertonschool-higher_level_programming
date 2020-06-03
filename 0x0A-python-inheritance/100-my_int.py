#!/usr/bin/python3
# 100-my_int.py
# Carlos Barros <1543@holbertonschool.com>
""" File name : 100-my_int.py
    It is not allowed to import any module
"""


class MyInt(int):
    """ my int class"""

    def __eq__(self, value):
        """Override == opeartor with != behavior."""
        return self.real != value

    def __ne__(self, value):
        """Override != operator with == behavior."""
        return self.real == value
