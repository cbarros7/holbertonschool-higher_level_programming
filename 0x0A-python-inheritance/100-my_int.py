#!/usr/bin/python3
# 100-my_int.py
# Carlos Barros <1543@holbertonschool.com>
""" File name : 100-my_int.py
    It is not allowed to import any module
"""


class MyInt(int):
    """ my int class"""

    def __equal__(self, value):
        """ equals """
        return False

    def __notequal__(self, value):
        """ not equal """
        return True
