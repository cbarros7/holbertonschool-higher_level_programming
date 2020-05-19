#!/usr/bin/python3
# 102-square.py
# Carlos Barros <1543@holbertonschool.com>
"""Compare 2 squares: """


class Square(object):
    """class variable size"""
    def __init__(self, size=0):
        """initialize size"""
        self.__size = size

    @property
    def size(self):
        """Property"""
        return self.__size

    @size.setter
    def size(self, value):
        """class variable size"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Define area"""
        return self.__size * self.__size

    def __eq__(self, other):
        """Equal area"""
        return self.area() == other.area()

    def __lt__(self, other):
        """Less"""
        return self.area() < other.area()

    def __gt__(self, other):
        """Greater"""
        return self.area() > other.area()

    def __ne__(self, other):
        """Different"""
        return self.area() != other.area()

    def __ge__(self, other):
        """Greater than or equals"""
        return self.area() >= other.area()

    def __le__(self, other):
        """Less than or equals"""
        return self.area() <= other.area()
