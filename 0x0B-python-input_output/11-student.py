#!/usr/bin/python3
# 11-student.py
# Carlos Barros <1543@holbertonschool.com>
""" File name : 11-student.py
"""


class Student(object):
    """Class student"""
    def __init__(self, first_name, last_name, age):
        """__init__ initialized constructor

        Args:
            first_name (str): first name
            last_name (str: last name
            age (int): age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary represt """
        return self.__dict__
