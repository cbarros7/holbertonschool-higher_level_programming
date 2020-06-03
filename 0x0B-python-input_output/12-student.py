#!/usr/bin/python3
# 12-student.py
# Carlos Barros <1543@holbertonschool.com>
""" File name : 12-student.py
"""
import json


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

    def to_json(self, attrs=None):
        """retrieves a dictionary represt """
        is_list_str = True
        if type(attrs) != list:
            is_list_str = False
        else:
            for i in attrs:
                if type(i) != str:
                    is_list_str = False
        if not is_list_str:
            return self.__dict__
        else:
            val = {}
            for attr in attrs:
                if attr in self.__dict__:
                    val[attr] = self.__dict__.get(attr)
            return val
