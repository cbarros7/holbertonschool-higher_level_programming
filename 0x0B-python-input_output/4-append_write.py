#!/usr/bin/python3
# 4-append_write.py
# Carlos Barros <1543@holbertonschool.com>
""" File name : 4-append_write.py
"""


def append_write(filename="", text=""):
    """append_write appends a string at the end of a text file (UTF8)

    Args:
        filename (str): Defaults to "".
        text (str): text to add. Defaults to "".
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
