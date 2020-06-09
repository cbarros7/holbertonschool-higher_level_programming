#!/usr/bin/python3
# test_rectangle.py
# Carlos Barros <1543@holbertonschool.com>
"""Defines unittests for rectangle.py."""
import unittest
import io
import sys
from io import StringIO
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Rectangle class."""

    def test_is_class(self):
        """ obj id increments """
        r1 = Rectangle(2, 2, 3, 1)
        self.assertTrue(type(r1) is Rectangle and issubclass(Rectangle, Base))

        r2 = Rectangle(2, 6, 4, 2)
        self.assertIsInstance(r2, Rectangle)

    def test_2_values(self):
        """checks for valid input """
        r1 = Rectangle(10, 2)
        r2 = Rectangle(1, 2)
        self.assertEqual(r1.id, r2.id - 1)

    def test_3_values(self):
        r1 = Rectangle(1, 2)
        r2 = Rectangle(2, 7)
        r3 = Rectangle(10, 2, 16)
        self.assertEqual(r1.id, r3.id - 2)

    def test_4_values(self):
        r1 = Rectangle(1, 2)
        r2 = Rectangle(2, 7)
        r3 = Rectangle(10, 2, 16)
        r4 = Rectangle(10, 2, 16, 5)
        self.assertEqual(r1.id, r4.id - 3)

    def test_5_values(self):
        r1 = Rectangle(1, 2)
        r2 = Rectangle(2, 7)
        r3 = Rectangle(10, 2, 16)
        r4 = Rectangle(10, 2, 16, 5)
        r5 = Rectangle(10, 2, 16, 5, 53)
        self.assertEqual(53, Rectangle(10, 2, 16, 5, 53).id)

    def one_arg_int_n(self):
        r1 = Rectangle(10, 2, 16, 4, -17)
        self.assertEqual(r6.id, -17)

    def one_arg_int_p(self):
        r1 = Rectangle(10, 2, 16, 4, 34)
        self.assertEqual(r6.id, 34)

    def str_arg(self):
        r7 = Rectangle(1, 11, 1, 1, "Holberton")
        self.assertEqual(r7.id, "Holberton")

    def one_arg(self):
        """checks for valid error"""
        with self.assertRaises(TypeError):
            Rectangle()

    def none_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(7, None)
            Rectangle(None, 6)

    def str_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 16, "Holberton")
            Rectangle(10, 2, 16, "Betty", "Holberton")

    def zero_arg(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 0, 0, 0, 0)

    def float_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 2.0, 1, 1, 12)

    def six_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 1, 1, 12, 5)


class TestRectangle_width(unittest.TestCase):
    """Unittests for testing initialization of Rectangle width attribute."""
    def width_none(self):
        with self.assertRaises(TypeError):
            Rectangle(None, 2, 1, 1, 12)

    def width_negative(self):
        with self.assertRaises(TypeError):
            Rectangle(-10, 2, 1, 1, 12)

    def width_arg(self):
        r = Rectangle(17, 11, 1, 1, "Holberton")
        self.assertEqual(r.width, 17)

    def width_str(self):
        with self.assertRaises(TypeError):
            Rectangle("Hello", 7, 0, 0, 1)

    def width_float_inf(self):
        with self.assertRaises(TypeError):
            Rectangle(float('inf'), 7, 0, 0, 1)

    def width_float_nan(self):
        with self.assertRaises(TypeError):
            Rectangle(float('nan'), 7, 0, 0, 1)

    def width_float_p(self):
        with self.assertRaises(TypeError):
            Rectangle(5.0, 7, 0, 0, 1)

    def width_dict(self):
        with self.assertRaises(TypeError):
            Rectangle({'a': 12, 'b': "Holberton"}, 2, 5, 7, 4)

    def width_tuple(self):
        with self.assertRaises(TypeError):
            Rectangle(("Holberton", ["World", "Betty", 3, 5],
                      {'a': 12, 'b': "Holberton"}), 2, 5, 7, 78)

    def width_list(self):
        with self.assertRaises(TypeError):
            Rectangle(['World', 'Betty', 3, 5, "Holberton"], 2, 5, 7, 90)


class TestRectangle_height(unittest.TestCase):
    """Unittests for testing initialization of Rectangle height attribute."""
    def height_none(self):
        with self.assertRaises(TypeError):
            Rectangle(4, None, 1, 1, 12)

    def height_negative(self):
        with self.assertRaises(TypeError):
            Rectangle(40, -2, 1, 1, 12)

    def height_arg(self):
        r = Rectangle(5, 56555566675, 0, 0, 1)
        self.assertEqual(r.height, 56555566675)

    def height_str(self):
        with self.assertRaises(TypeError):
            Rectangle(5, "Holberton", 0, 0, 1)

    def height_float_inf(self):
        with self.assertRaises(TypeError):
            Rectangle(6, float('inf'), 0, 0, 1)

    def height_float_nan(self):
        with self.assertRaises(TypeError):
            Rectangle(5, float('nan'), 0, 0, 1)

    def height_float_p(self):
        with self.assertRaises(TypeError):
            Rectangle(5, 7.54, 0, 0, 1)

    def height_dict(self):
        with self.assertRaises(TypeError):
            Rectangle(5, {'a': 12, 'b': "Holberton"}, 5, 7, 4)

    def height_tuple(self):
        with self.assertRaises(TypeError):
            Rectangle(80, ("Holberton", ["World", "Betty", 3, 5],
                      {'a': 12, 'b': "Holberton"}), 5, 7, 78)

    def height_list(self):
        with self.assertRaises(TypeError):
            Rectangle(66, ['World', 'Betty', 3, 5, "Holberton"], 5, 7, 90)


class TestRectangle_x(unittest.TestCase):
    """Unittests for testing initialization of Rectangle x attribute."""
    def x_none(self):
        with self.assertRaises(TypeError):
            Rectangle(3, 2, None, 1, 12)

    def x_negative(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 2, -51, 1, 12)

    def x_arg(self):
        r = Rectangle(17, 11, 0, 1, "Holberton")
        self.assertEqual(r.x, 0)

    def x_str(self):
        with self.assertRaises(TypeError):
            Rectangle(5, 6, "Holberton", 0, 1)

    def x_float_inf(self):
        with self.assertRaises(TypeError):
            Rectangle(6, 8, float('inf'), 0, 1)

    def x_float_nan(self):
        with self.assertRaises(TypeError):
            Rectangle(5, 86, float('nan'), 0, 1)

    def x_float_p(self):
        with self.assertRaises(TypeError):
            Rectangle(5, 7, 43.43, 0, 1)

    def x_dict(self):
        with self.assertRaises(TypeError):
            Rectangle(5, 7, {'a': 12, 'b': "Holberton"}, 5, 4)

    def x_tuple(self):
        with self.assertRaises(TypeError):
            Rectangle(80, 6, ("Holberton", ["World", "Betty", 3, 5],
                      {'a': 12, 'b': "Holberton"}), 7, 78)

    def x_list(self):
        with self.assertRaises(TypeError):
            Rectangle(66, 56, ['World', 'Betty', 3, 5, "Holberton"], 7, 90)


class TestRectangle_y(unittest.TestCase):
    """Unittests for testing initialization of Rectangle y attribute."""
    def y_none(self):
        with self.assertRaises(TypeError):
            Rectangle(3, 2, 6, None, 12)

    def y_negative(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 6, -65, 12)

    def y_arg(self):
        r = Rectangle(17, 11, 1, 775, "Holberton")
        self.assertEqual(r.y, 775)

    def y_float_inf(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 2, float('inf'), 1, 5)

    def y_float_nan(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 2, float('nan'), 1, 5)

    def y_str(self):
        with self.assertRaises(TypeError):
            Rectangle(5, 6, 5, "Holberton", 1)

    def y_float_p(self):
        with self.assertRaises(TypeError):
            Rectangle(5, 7, 43, 6.3, 1)

    def y_dict(self):
        with self.assertRaises(TypeError):
            Rectangle(5, 7, 54, {'a': 12, 'b': "Holberton"}, 4)

    def y_tuple(self):
        with self.assertRaises(TypeError):
            Rectangle(80, 6, 653, ("Holberton", ["World", "Betty", 3, 5],
                      {'a': 12, 'b': "Holberton"}), 78)

    def y_list(self):
        with self.assertRaises(TypeError):
            Rectangle(66, 56, 54, ['World', 'Betty', 3, 5, "Holberton"], 90)


class TestRectangle_id(unittest.TestCase):
    """Unittests for testing initialization of Rectangle y attribute."""

    def wrong_id(self):
        with self.assertRaises(NameError):
            Rectangle(10, 2, 1, 1, fdfdfdfd)

    def id_str(self):
        r = Rectangle(3, 2, 5, 7, "Hello")
        self.assertEqual("HEllo", r.id)

    def id_dict(self):
        r = Rectangle(3, 2, 5, 7, {'a': 12, 'b': "Holberton"})
        self.assertEqual({'a': 12, 'b': "Holberton"}, r.id)

    def id_tuple(self):
        r = Rectangle(3, 2, 5, 7, ("Holberton", ["World", "Betty", 3, 5],
                      {'a': 12, 'b': "Holberton"}))
        self.assertEqual(("Holberton", ["World", "Betty", 3, 5],
                          {'a': 12, 'b': "Holberton"}), r.id)

    def id_list(self):
        r = Rectangle(3, 2, 5, 7, ['World', 'Betty', 3, 5, "Holberton"])
        self.assertEqual(['World', 'Betty', 3, 5, "Holberton"], r.id)


class TestRectangle_area(unittest.TestCase):
    """Unittests for testing area of the Rectangle class."""
    def test_area_int(self):
        r = Rectangle(3, 2)
        self.assertEqual(6, r.area())

    def area_int(self):
        r = Rectangle(2, 10, 0, 0, 6)
        self.assertEqual(20, r.area())

    def change_value_area(self):
        r = Rectangle(2, 10, 0, 0, 6)
        r.width = 8
        r.height = 7
        self.assertEqual(56, r.area())

    def missing_width(self):
        with self.assertRaises(TypeError):
            r = Rectangle(None, 10, 0, 0, 6)

    def missing_width_2(self):
        r = Rectangle(1, 10, 0, 0, 6)
        with self.assertRaises(TypeError):
            r(5)

    def missing_height(self):
        with self.assertRaises(TypeError):
            r = Rectangle(4, None, 0, 0, 6)

    def missing_height_2(self):
        r = Rectangle(4, 5, 0, 0, 6)
        with self.assertRaises(TypeError):
            r(7)


class TestRectangle_display(unittest.TestCase):
    """new class"""

    @staticmethod
    def display_stdout(rect, method):
        """display_stdout and returns text printed to stdout.
        Args:
            rect (Rectangle): The Rectangle to print to stdout.
            method (str): The method to run on rect.
        Returns:
            The text printed to stdout
        """
        display_stdout = io.StringIO()
        sys.stdout = display_stdout
        if method == "print":
            print(rect)
        else:
            rect.display()
        sys.stdout = sys.__stdout__
        return display_stdout

    def test_print_width_height(self):
        r = Rectangle(4, 6)
        capture = TestRectangle_display.display_stdout(r, "print")
        correct = "[Rectangle] ({}) 0/0 - 4/6\n".format(r.id)
        self.assertEqual(correct, capture.getvalue())

    def test_print_width_height_x(self):
        r = Rectangle(3, 6, 4)
        capture = TestRectangle_display.display_stdout(r, "print")
        correct = "[Rectangle] ({}) 4/0 - 3/6\n".format(r.id)
        self.assertEqual(correct, capture.getvalue())

    def test_method_width_height_x_y(self):
        r = Rectangle(15, 38, 25, 45)
        correct = "[Rectangle] ({}) 25/45 - 15/38".format(r.id)
        self.assertEqual(correct, str(r))

    def test_method_width_height_x_y_id(self):
        r = Rectangle(30, 45, 23, 4, 4)
        self.assertEqual("[Rectangle] (4) 23/4 - 30/45", str(r))

    def test_method_changed_attributes(self):
        r = Rectangle(12, 23, 67, 64, [5])
        r.width = 75
        r.height = 43
        r.x = 13
        r.y = 75
        self.assertEqual("[Rectangle] ([5]) 13/75 - 75/43", str(r))

    def test_method_one_arg(self):
        r = Rectangle(1, 6, 4, 2, 9)
        with self.assertRaises(TypeError):
            r.__str__(1)

    def test_float_one_arg(self):
        r = Rectangle(1, 8, 4, 2, 9)
        with self.assertRaises(TypeError):
            r.__str__(34.54)

    def test_display_width_height(self):
        r = Rectangle(2, 4, 0, 0, 0)
        capture = TestRectangle_display.display_stdout(r, "display")
        self.assertEqual("##\n##\n##\n##\n", capture.getvalue())

    def test_display_width_height_x_y(self):
        r = Rectangle(4, 3, 1, 0, 0)
        capture = TestRectangle_display.display_stdout(r, "display")
        self.assertEqual(" ####\n ####\n ####\n", capture.getvalue())

    def test_display_width_height_x_y_2(self):
        r = Rectangle(6, 2, 0, 1, 0)
        capture = TestRectangle_display.display_stdout(r, "display")
        self.assertEqual("\n######\n######\n", capture.getvalue())

    def test_one_arg(self):
        r = Rectangle(43, 62, 34, 23, 32)
        with self.assertRaises(TypeError):
            r.display(1)


class TestRectangle_update_args(unittest.TestCase):
    """Unittests for testing update args method of the Rectangle class."""

    def test_update_args_zero(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update()
        self.assertEqual("[Rectangle] (10) 10/10 - 10/10", str(r))

    def test_update_one_arg(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(13)
        self.assertEqual("[Rectangle] (13) 10/10 - 10/10", str(r))

    def test_update_width_arg(self):
        r = Rectangle(10, 3, 10, 10, 10)
        r.update(13)
        self.assertEqual("[Rectangle] (13) 10/10 - 10/3", str(r))

    def test_update_height_arg(self):
        r = Rectangle(10, 10, 3, 10, 10)
        r.update(13)
        r.height = 53
        r.update(5)
        self.assertEqual("[Rectangle] (5) 3/10 - 10/53", str(r))

    def test_two_update(self):
        r = Rectangle(10, 10, 3, 10, 10)
        r.update(13)
        r.height = 53
        r.update(5)
        r.id = 32
        self.assertEqual("[Rectangle] (32) 3/10 - 10/53", str(r))

    def test_update_args_twice(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5, 6)
        r.update(6, 5, 4, 3, 2, 89)
        self.assertEqual("[Rectangle] (6) 3/2 - 5/4", str(r))

    def test_update_width_zero(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaises(ValueError):
            r.update(89, 0)

    def test_update_width_none(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaises(TypeError):
            r.update(89, None)

    def test_update_height_none(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaises(TypeError):
            r.update(89, 3, None)

    def test_update_args_invalid_width(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaises(TypeError):
            r.update(89, "Holberton")

    def test_update_args_invalid_height(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaises(TypeError):
            r.update(89, 53, "Betty")

    def test_update_args_negative_width(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaises(ValueError):
            r.update(89, -53, 4)

    def test_update_args_negative_height(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaises(ValueError):
            r.update(89, 53, -4)

    def test_update_args_float_height(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaises(TypeError):
            r.update(89, 5.3, 4.4)

    def test_update_args_width_before_x(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaises(TypeError):
            r.update(89, "invalid", 1, "invalid")

    def test_update_args_str_x_y(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaises(TypeError):
            r.update(89, 5, 4, "Betty", "Holberton")

    def test_update_args_str_all(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaises(TypeError):
            r.update("Hello", "Softaware", "Holberton", "Betty")


class TestRectangle_update_kwargs(unittest.TestCase):
    """Unittests for testing update kwargs method of the Rectangle class."""
    def test_update_id_kwargs(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=5)
        self.assertEqual("[Rectangle] (5) 10/10 - 10/10", str(r))

    def test_update_id_width_kwargs(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(width=8, id=7)
        self.assertEqual("[Rectangle] (7) 10/10 - 8/10", str(r))

    def test_update_height_x_kwargs(self):
        r = Rectangle(54, 43, 3, 10, 15)
        r.height = 86
        r.update(x=29)
        self.assertEqual("[Rectangle] (15) 29/10 - 54/86", str(r))

    def test_update_kwargs_twice(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(width=89, id=2, height=3, x=4, y=5)
        r.update(height=6, width=5, x=4, id=3, y=2)
        self.assertEqual("[Rectangle] (3) 4/2 - 5/6", str(r))

    def test_update_x_zero(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(x=0, width=32, y=5, id=8)
        self.assertEqual("[Rectangle] (8) 0/5 - 32/10", str(r))

    def test_update_y_zero(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(x=8, width=32, y=0, id=8)
        self.assertEqual("[Rectangle] (8) 8/0 - 32/10", str(r))

    def test_update_x_y_zero(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(x=0, width=32, y=0, id=8)
        self.assertEqual("[Rectangle] (8) 0/0 - 32/10", str(r))


class TestRectangle_update_errors_kwargs(unittest.TestCase):
    """Unittests for testing update errors kwargs
    method of the Rectangle class."""

    def test_update_width_zero(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaises(ValueError):
            r.update(x=89, width=0)

    def test_update_width_none(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaises(TypeError):
            r.update(id=89, width=None)

    def test_update_width_float_inf(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaises(TypeError):
            r.update(id=89, width=float('inf'), height=5, x=23)

    def test_update_width_float_nan(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaises(TypeError):
            r.update(id=89, width=float('nan'), height=5, x=23)

    def test_update_width_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaises(ValueError):
            r.update(id=89, width=-8, height=5, x=23)

    def test_update_width_dict(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaises(TypeError):
            r.update(width={'name': "Carlos", 'age': 24},
                     id=2, height=4, y=6)

    def test_update_width_list(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaises(TypeError):
            r.update(width=["Carlos", 24, "Software"],
                     id=2, height=4, y=6)

    def test_update_height_float_inf(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaises(TypeError):
            r.update(id=89, height=float('inf'), width=5, x=23)

    def test_update_heigth_float_nan(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaises(TypeError):
            r.update(id=89, height=float('nan'), width=5, x=23)

    def test_update_height_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaises(ValueError):
            r.update(id=89, width=8, height=-5, x=23)

    def test_update_height_zero(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaises(ValueError):
            r.update(x=89, width=32, y=5, id=8, height=0)

    def test_update_height_none(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaises(TypeError):
            r.update(y=89, x=3, height=None)

    def test_update_height_dict(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaises(TypeError):
            r.update(height={'name': "Carlos", 'age': 24},
                     id=2, width=4, y=6)

    def test_update_height_list(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaises(TypeError):
            r.update(height=["Carlos", 24, "Software"],
                     id=2, width=4, y=6)

    def test_update_x_none(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaises(TypeError):
            r.update(y=89, id=3, height=7, x=None)

    def test_update_x_float_inf(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaises(TypeError):
            r.update(id=89, x=float('inf'), width=5, height=23)

    def test_update_x_float_nan(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaises(TypeError):
            r.update(id=89, x=float('nan'), width=5, height=23)

    def test_update_x_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaises(ValueError):
            r.update(id=89, width=8, height=5, x=-23)

    def test_update_x_dict(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaises(TypeError):
            r.update(x={'name': "Carlos", 'age': 24},
                     id=2, width=4, y=6, height=50)

    def test_update_x_list(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaises(TypeError):
            r.update(x=["Carlos", 24, "Software"],
                     id=2, width=4, y=6, height=30)

    def test_update_y_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaises(ValueError):
            r.update(id=89, width=-8, y=-97, height=5, x=23)

    def test_update_y_none(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaises(TypeError):
            r.update(x=89, id=3, height=7, y=None)

    def test_update_y_float_inf(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaises(TypeError):
            r.update(id=89, y=float('inf'), width=5, height=23)

    def test_update_y_float_nan(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaises(TypeError):
            r.update(id=89, y=float('nan'), width=5, height=23)

    def test_update_y_dict(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaises(TypeError):
            r.update(y={'name': "Carlos", 'age': 24},
                     id=2, width=4, x=6, height=50)

    def test_update_y_list(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaises(TypeError):
            r.update(y=["Carlos", 24, "Software"],
                     id=2, width=4, x=6, height=30)


class TestRectangle_to_dictionary(unittest.TestCase):
    """Unittests for testing to dictionary for rectangle class."""

    def test_to_dictionary_output(self):
        r = Rectangle(10, 2, 1, 9, 5)
        correct = {'x': 1, 'y': 9, 'id': 5, 'height': 2, 'width': 10}
        self.assertDictEqual(correct, r.to_dictionary())

    def test_to_dictionary_no_object_changes(self):
        r1 = Rectangle(10, 2, 1, 9, 5)
        r2 = Rectangle(5, 9, 1, 2, 10)
        r2.update(**r1.to_dictionary())
        self.assertNotEqual(r1, r2)

    def test_to_dictionary_arg(self):
        r = Rectangle(10, 2, 4, 1, 2)
        with self.assertRaises(TypeError):
            r.to_dictionary(1)

    def test_input_id(self):
        """ Test if input id gets set """
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)

    def test_width_check(self):
        """ Test width for rect """
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.width, 10)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.width, 2)

        r3 = Rectangle(5, 2, 0, 0, 12)
        self.assertEqual(r3.width, 5)

    def test_check_width_Error_1(self):
        """ Test TypeError for width in rect """
        self.assertRaisesRegex(
            TypeError,
            'width must be an integer',
            Rectangle,
            'string', 2, 0, 0, 12
        )

    def test_check_width_TypeError_02(self):
        """Test TypeError for width in Rectangle"""
        self.assertRaisesRegex(
            TypeError,
            'width must be an integer',
            Rectangle,
            [6, 4, 9, 9], 2, 0, 0, 12
        )

    def test_check_x(self):
        """Test x of rect"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.x, 0)

        r2 = Rectangle(2, 10, 6)
        self.assertEqual(r2.x, 6)

        r3 = Rectangle(5, 2, 3, 9, 12)
        self.assertEqual(r3.x, 3)

        r4 = Rectangle(5, 2, 0, 3, 12)
        self.assertEqual(r4.x, 0)

    def test_check_x_TypeError_01(self):
        """Test TypeError for x in Rect"""
        self.assertRaisesRegex(
            TypeError,
            'x must be an integer',
            Rectangle,
            4, 2, 'string''', 0, 12
        )

    def test_check_x_TypeError_02(self):
        """Test TypeError for x in rect"""
        self.assertRaisesRegex(
            TypeError,
            'x must be an integer',
            Rectangle,
            4, 2, [1, 2, 3, 4], 0, 12
        )

    def test_check_x_ValueError(self):
        """Test ValueError for x in Rect"""
        self.assertRaisesRegex(
            ValueError,
            'x must be >= 0',
            Rectangle,
            4, 2, -1, 0, 12
        )

    def test_check_y(self):
        """Test y of rect"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.y, 0)

        r2 = Rectangle(2, 10, 6, 4)
        self.assertEqual(r2.y, 4)

        r3 = Rectangle(5, 2, 3, 9, 12)
        self.assertEqual(r3.y, 9)

        r4 = Rectangle(5, 2, 3, 0, 12)
        self.assertEqual(r4.y, 0)

    def test_check_y_TypeError_01(self):
        """Test TypeError for y in Rect"""
        self.assertRaisesRegex(
            TypeError,
            'y must be an integer',
            Rectangle,
            4, 2, 0, 'string', 12
        )

    def test_check_y_TypeError_02(self):
        """Test TypeError for y in Rectangle"""
        self.assertRaisesRegex(
            TypeError,
            'y must be an integer',
            Rectangle,
            4, 2, 0, [1, 2, 3, 4], 12
        )

    def test_check_y_TypeError_(self):
        """Test TypeError for y in Rect"""
        self.assertRaisesRegex(
            ValueError,
            'y must be >= 0',
            Rectangle,
            4, 2, 0, -6, 12
        )

    def test_update(self):
        """update test"""
        output = StringIO()
        sys.stdout = output
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89)
        r1.update(89, 2)
        r1.update(89, 2, 3)
        r1.update(89, 2, 3, 4)
        r1.update(89, 2, 3, 4, 5)
        print(r1)
        sys.stdout = sys.__stdout__
        assert output.getvalue() == "[Rectangle] (89) 4/5 - 2/3\n"

    def test_update_extra(self):
        """update with etra parameters"""
        output = StringIO()
        sys.stdout = output
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89, 2, 3, 4, 5, 6, 7)
        print(r1)
        sys.stdout = sys.__stdout__
        assert output.getvalue() == "[Rectangle] (89) 4/5 - 2/3\n"

if __name__ == "__main__":
    unittest.main()
