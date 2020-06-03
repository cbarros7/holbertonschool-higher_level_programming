#!/usr/bin/python3
# 2-read_lines.py
# Carlos Barros <1543@holbertonschool.com>
""" File name : 2-read_lines.py
    Use the with statement
    It is not allowed to import any module
"""


def read_lines(filename="", nb_lines=0):
    """read_lines reads n lines of a text file (UTF8) and prints it to stdout

    Args:
        filename (str): content of the file. Defaults to "".
        nb_lines (int): number lines. Defaults to 0.

    Returns:
        str: returns the number of lines of a text file
    """
    line_count = 0
    with open(filename, 'r', encoding='utf-8') as f:
        if nb_lines <= 0:
            print(f.read(), end="")
        for line in f:
            if line_count < nb_lines:
                print(line, end="")
                line_count += 1
