#!/usr/bin/python3
# 12-student.py
# Carlos Barros <1543@holbertonschool.com>
""" File name : 12-student.py
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

    def to_json(self, attrs=None):
        """retrieves a dictionary represt """
        if attrs is None:
            return self.__dict__
        dictionary = {}
        for key, value in self.__dict__.items():
            if key in attrs:
                dictionary[key] = value
        return dictionary

    def reload_from_json(self, json):
        """Replace all attributes of the Student.
        Args:
            json (dict): The key/value pairs to replace attributes with.
        """
        for key, value in json.items():
            setattr(self, key, value)
