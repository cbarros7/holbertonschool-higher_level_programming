#!/usr/bin/python3
# 1-my_list.py
# Carlos Barros <1543@holbertonschool.com>
""" File name : 1-my_list.py
    It is not allowed to import any module
"""


class MyList(list):
    """Define class my list"""
    def print_sorted(self):
        """print sorted list"""
        print(sorted(self))
