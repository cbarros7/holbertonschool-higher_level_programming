#!/usr/bin/python3
# 0-read_file.py
# Carlos Barros <1543@holbertonschool.com>
""" File name : 0-read_file.py
    Use the with statement
    It is not allowed to import any module
"""


def read_file(filename=""):
    """read_file reads a text file (UTF8) and prints it to stdout

    Args:
        filename (str): content of the file. Defaults to "".
    """
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read(), end="")
