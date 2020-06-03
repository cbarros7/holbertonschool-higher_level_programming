#!/usr/bin/python3
# 1-my_list.py
# Carlos Barros <1543@holbertonschool.com>
""" File name : 1-my_list.py
    It is not allowed to import any module
"""


class MyList(list):
    """Implements sorted printing for the built-in list class."""

    def print_sorted(self):
        """Print a list in sorted ascending order."""
        print(sorted(self))
