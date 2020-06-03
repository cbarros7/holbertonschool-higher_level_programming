#!/usr/bin/python3
# 1-number_of_lines.py
# Carlos Barros <1543@holbertonschool.com>
""" File name : 1-number_of_lines.py
    Use the with statement
    It is not allowed to import any module
"""


def number_of_lines(filename=""):
    """number_of_lines: returns the number of lines of a text file:

    Args:
        filename (str): content of the file. Defaults to "".
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return len(f.readlines())
