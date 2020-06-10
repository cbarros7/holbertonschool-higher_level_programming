#!/usr/bin/python3
# test_base.py
# Carlos Barros <1543@holbertonschool.com>
"""Defines unittests for base.py."""
import unittest
import os
import json
import sys
from io import StringIO
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Base class."""

    def test_incrementation(self):
        """ obj id increments """
        Base._Base__nb_objects = 0

        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

        b3 = Base()
        self.assertEqual(b3.id, 3)

    def test_inputs(self):
        """checks for valid input """
        Base._Base__nb_objects = 0

        b_zero = Base()
        self.assertEqual(b_zero.id, 1)

        b_int = Base(17)
        self.assertEqual(b_int.id, 17)

    def test_negative(self):
        b_negint = Base(-29)
        self.assertEqual(b_negint.id, -29)

    def test_float(self):
        b_float_n = Base(-6.7)
        self.assertEqual(b_float_n.id, -6.7)

        b_float_p = Base(7.7)
        self.assertEqual(b_float_p.id, 7.7)

    def test_id_public(self):
        b = Base(12)
        b.id = 15
        self.assertEqual(15, b.id)

    def test_unique_id(self):
        self.assertEqual(12, Base(12).id)

    def test_str(self):
        """checks for valid input """
        b_string = Base("Holberton")
        self.assertEqual(b_string.id, "Holberton")

    def test_dict_id(self):
        b_dict = Base({'a': 12, 'b': "Holberton"})
        self.assertEqual(b_dict.id, {'a': 12, 'b': "Holberton"})

    def test_tuple_id(self):
        b_tuple = Base(("Holberton", ["World", "Betty", 3, 5],
                       {'a': 12, 'b': "Holberton"}))
        self.assertEqual(b_tuple.id, ("Holberton", ["World", "Betty", 3, 5],
                         {'a': 12, 'b': "Holberton"}))

    def test_list_id(self):
        b_list = Base(['World', 'Betty', 3, 5, "Holberton"])
        self.assertEqual(b_list.id, (['World', 'Betty', 3, 5, "Holberton"]))

    def test_range(self):
        b_range = Base(range(4))
        self.assertEqual(b_range.id, range(0, 4))

    def test_float_inf(self):
        b_float_inf = Base(float('inf'))
        self.assertEqual(b_float_inf.id, float('inf'))

    def test_NaN_id(self):
        self.assertNotEqual(float('nan'), Base(float('nan')).id)

    def test_error(self):
        """checks for valid error"""
        with self.assertRaises(TypeError):
            Base(7, 7)

        with self.assertRaises(TypeError):
            Base(7, None)

        with self.assertRaises(TypeError):
            Base(None, 6)


class TestBase_to_json_string(unittest.TestCase):
    """Unittests for testing to_json_string method of Base class."""

    def test_to_json_string_rectangle_type(self):
        r = Rectangle(10, 7, 2, 8, 6)
        self.assertEqual(str, type(Base.to_json_string([r.to_dictionary()])))

    def test_to_json_string_rectangle_one_dict(self):
        r = Rectangle(10, 7, 2, 8, 6)
        self.assertTrue(len(Base.to_json_string([r.to_dictionary()])) == 53)

    def test_to_json_string_rectangle_two_dicts(self):
        r1 = Rectangle(2, 3, 5, 19, 2)
        r2 = Rectangle(4, 2, 4, 1, 12)
        list_dicts = [r1.to_dictionary(), r2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 106)

    def test_to_json_string_square_type(self):
        s = Square(10, 2, 3, 4)
        self.assertEqual(str, type(Base.to_json_string([s.to_dictionary()])))

    def test_to_json_string_square_one_dict(self):
        s = Square(10, 2, 3, 4)
        self.assertTrue(len(Base.to_json_string([s.to_dictionary()])) == 39)

    def test_to_json_string_square_two_dicts(self):
        s1 = Square(10, 2, 3, 4)
        s2 = Square(4, 5, 21, 2)
        list_dicts = [s1.to_dictionary(), s2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 78)

    def test_to_json_string_empty_list(self):
        self.assertEqual("[]", Base.to_json_string([]))

    def test_to_json_string_none(self):
        self.assertEqual("[]", Base.to_json_string(None))

    def test_to_json_string_no_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_to_json_string_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([], 1)


class TestBase_save_to_file(unittest.TestCase):
    """Unittests for testing save_to_file method of Base class."""

    @classmethod
    def tearDown(self):
        """Delete any created files."""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass
        try:
            os.remove("Base.json")
        except IOError:
            pass

    def test_save_to_file_one_rectangle(self):
        r = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 53)

    def test_save_to_file_two_rectangles(self):
        r1 = Rectangle(10, 7, 2, 8, 5)
        r2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 105)

    def test_save_to_file_one_square(self):
        s = Square(10, 7, 2, 8)
        Square.save_to_file([s])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)

    def test_save_to_file_two_squares(self):
        s1 = Square(10, 7, 2, 8)
        s2 = Square(8, 1, 2, 3)
        Square.save_to_file([s1, s2])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 77)

    def test_save_to_file_cls_name_for_filename(self):
        s = Square(10, 7, 2, 8)
        Base.save_to_file([s])
        with open("Base.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)

    def test_save_to_file_overwrite(self):
        s = Square(9, 2, 39, 2)
        Square.save_to_file([s])
        s = Square(10, 7, 2, 8)
        Square.save_to_file([s])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)

    def test_save_to_file_None(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_empty_list(self):
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def test_save_to_file_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Square.save_to_file([], 1)


class TestBase_from_json_string(unittest.TestCase):
    """Unittests for testing from_json_string method of Base class."""

    def test_from_json_string_type(self):
        list_input = [{"id": 89, "width": 10, "height": 4}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list, type(list_output))

    def test_from_json_string_one_rectangle(self):
        list_input = [{"id": 89, "width": 10, "height": 4, "x": 7}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_two_rectangles(self):
        list_input = [
            {"id": 89, "width": 10, "height": 4, "x": 7, "y": 8},
            {"id": 98, "width": 5, "height": 2, "x": 1, "y": 3},
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_one_square(self):
        list_input = [{"id": 89, "size": 10, "height": 4}]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_two_squares(self):
        list_input = [
            {"id": 89, "size": 10, "height": 4},
            {"id": 7, "size": 1, "height": 7}
        ]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_None(self):
        self.assertEqual([], Base.from_json_string(None))

    def test_from_json_string_empty_list(self):
        self.assertEqual([], Base.from_json_string("[]"))

    def test_from_json_string_no_args(self):
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def test_from_json_string_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.from_json_string([], 1)

    def test_load_from_file(self):
        """Test load_from_file with non-existant file"""
        obj = Base.load_from_file()
        self.assertEqual(obj, [])

    def test_from_json_string_none(self):
        """Test from_json_string with None"""
        self.assertEqual(Base.from_json_string(None), [])

    def test_to_json_string_empty(self):
        """Test inherited test_to_json_string() with empty list and None"""
        self.assertEqual(Base.to_json_string([]), '[]')
        self.assertEqual(Base.to_json_string(None), '[]')

    def test_save_to_file_none(self):
        """Test save_to_file() with None"""
        Base.save_to_file(None)
        with open("Base.json", "r") as f:
            bases = json.load(f)
            self.assertEqual(len(bases), 0)
            self.assertEqual(bases, [])


class TestBase_create(unittest.TestCase):
    """Unittests for testing create method of Base class."""

    def test_create_rectangle_original(self):
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(r1))

    def test_create_rectangle_new(self):
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(r2))

    def test_create_rectangle_is(self):
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertIsNot(r1, r2)

    def test_create_rectangle_equals(self):
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertNotEqual(r1, r2)

    def test_create_square_original(self):
        s1 = Square(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual("[Square] (7) 5/1 - 3", str(s1))

    def test_create_square_new(self):
        s1 = Square(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual("[Square] (7) 5/1 - 3", str(s2))

    def test_create_square_is(self):
        s1 = Square(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertIsNot(s1, s2)

    def test_create_square_equals(self):
        s1 = Square(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertNotEqual(s1, s2)

    def test_load_from_file(self):
        """Test load_from_file method"""

        r1 = Rectangle(3, 5, 2, 4, 1)
        dr1 = r1.to_dictionary()
        r2 = Rectangle(3, 5, 2, 4)
        dr2 = r2.to_dictionary()
        r3 = Rectangle(3, 10)
        dr3 = r3.to_dictionary()
        s1 = Square(3, 2, 4, 1)
        ds1 = s1.to_dictionary()
        s2 = Square(3, 2, 4)
        ds2 = s2.to_dictionary()
        s3 = Square(3)
        ds3 = s3.to_dictionary()
        Rectangle.save_to_file([r1, r2, r3])
        list_objs_r = Rectangle.load_from_file()
        Square.save_to_file([s1, s2, s3])
        list_objs_s = Square.load_from_file()

        self.assertIsInstance(list_objs_r[0], Rectangle)
        self.assertDictEqual(list_objs_r[0].to_dictionary(), dr1)

        self.assertIsInstance(list_objs_r[1], Rectangle)
        self.assertDictEqual(list_objs_r[1].to_dictionary(), dr2)

        self.assertIsInstance(list_objs_r[2], Rectangle)
        self.assertDictEqual(list_objs_r[2].to_dictionary(), dr3)

        self.assertIsInstance(list_objs_s[0], Square)
        self.assertDictEqual(list_objs_s[0].to_dictionary(), ds1)

        self.assertIsInstance(list_objs_s[1], Square)
        self.assertDictEqual(list_objs_s[1].to_dictionary(), ds2)

        self.assertIsInstance(list_objs_s[2], Square)
        self.assertDictEqual(list_objs_s[2].to_dictionary(), ds3)

if __name__ == "__main__":
    unittest.main()
