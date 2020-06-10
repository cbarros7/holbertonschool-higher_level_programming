#!/usr/bin/python3
# base.py
# Carlos Barros <1543@holbertonschool.com>
"""Define Base class"""
import json
from os import path


class Base(object):
    """Base: Class define base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """__init__ initialized constructor

        Args:
            id (int): Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dict):
        """Return the JSON serialization of a list of dicts.

        Args:
            list_dictionaries (list): A list of dictionaries.
        """
        if list_dict is None or len(list_dict) == 0:
            return "[]"
        return json.dumps(list_dict)

    @classmethod
    def save_to_file(cls, list_objs):
        """save_to_file: writes the JSON string representation of list_objs to a file

        Args:
            list_objs (list): list of instances who inherits of Base
        """
        with open(cls.__name__ + '.json', 'w', encoding='utf-8') as f:
            if list_objs is None:
                f.write('[]')
            else:
                f.write(cls.to_json_string([o.to_dictionary()
                        for o in list_objs]))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if not isinstance(json_string, str) or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ Returns a list of instances"""
        file_name = cls.__name__ + '.json'
        if path.isfile(file_name):
            with open(file_name, 'r', encoding='utf-8') as f:
                dictionary = cls.from_json_string(f.read())
            return[cls.create(**obj) for obj in dictionary]
        return []
