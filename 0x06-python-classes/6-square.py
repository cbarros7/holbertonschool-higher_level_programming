#!/usr/bin/python3
# 6-square.py
# Carlos Barros <1543@holbertonschool.com>
"""Coordinates of a square: """


class Square(object):
    """class variable size"""
    def __init__(self, size=0, position=(0, 0)):
        """initialize size"""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Property for size"""
        return self.__size

    @size.setter
    def size(self, value):
        """class variable size"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Property for position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Property for position"""
        error = "position must be a tuple of 2 positive integers"
        if type(value) is not tuple:
            raise TypeError(error)
        for i in range(len(value)):
            if value[i] < 0:
                raise ValueError("size must be >= 0")
            if len(value) != 2:
                raise TypeError(error)
        self.__position = value

    def area(self):
        """Define area"""
        return self.__size * self.__size

    def my_print(self):
        """Print vector with # and spaces"""
        if self.__size > 0:
            for k in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for space in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()
        else:
            print()
