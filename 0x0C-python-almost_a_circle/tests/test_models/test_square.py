#!/usr/bin/python3
# test_square.py
# Carlos Barros <1543@holbertonschool.com>
"""Defines unittests for square.py."""
import unittest
import io
import sys
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Square class."""

    def test_is_base(self):
        self.assertIsInstance(Square(10), Base)

    def test_is_rectangle(self):
        self.assertIsInstance(Square(4), Rectangle)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Square()

    def test_3_values(self):
        s1 = Square(1, 2)
        s2 = Square(2, 7)
        s3 = Square(10, 2, 16)
        self.assertEqual(s1.id, s3.id - 2)

    def test_4_values(self):
        s1 = Square(1, 2)
        s2 = Square(2, 7)
        s3 = Square(10, 2, 16)
        s4 = Square(6, 4, 54)
        self.assertEqual(s1.id, s4.id - 3)

    def test_one_line(self):
        self.assertEqual(4, Square(1, 2, 6, 4).id)

    def test_id_str(self):
        self.assertEqual("Holberton", Square(1, 2, 6, "Holberton").id)

    def test_size_getter(self):
        self.assertEqual(6, Square(6, 2, 3, 9).size)

    def test_size_getter_1(self):
        s = Square(6, 2, 3, 9)
        s.update(size=43)
        self.assertEqual(43, s.size)

    def test_x_getter(self):
        self.assertEqual(2, Square(6, 2, 3, 9).x)

    def test_x_getter_1(self):
        s = Square(6, 2, 3, 9)
        s.update(x=23)
        self.assertEqual(23, s.x)

    def test_y_getter(self):
        self.assertEqual(3, Square(6, 2, 3, 9).y)

    def test_y_getter_1(self):
        s = Square(6, 2, 3, 9)
        s.update(y=57)
        self.assertEqual(57, s.y)

    def test_zero_x_y(self):
        s = Square(1)
        self.assertTrue(s.y == 0 and s.x == 0)

    def test_zero_x_y(self):
        s = Square(1, 5, 6, 0)
        self.assertTrue(s.y == 6 and s.x == 5 and
                        s.id == 0 and s.size == 1)

    def test_zero_x_y(self):
        s = Square(75, 54, 32, -52)
        self.assertTrue(s.id == -52)

    def test_update_all(self):
        s = Square(6, 2, 3, 9)
        s.update(y=57, id=4, x=79, size=76)
        self.assertTrue(s.x == 79 and s.id == 4 and
                        s.y == 57 and s.size == 76)

    def test_none_size(self):
        with self.assertRaises(TypeError):
            Square(None, 2)

    def test_y_id(self):
        with self.assertRaises(TypeError):
            Square(10, 2, "Hello", 5)

    def test_float_all(self):
        with self.assertRaises(TypeError):
            Square(3.0, 5.0, 4.0, 62.0)

    def test_six_arg(self):
        with self.assertRaises(TypeError):
            Square(10, 2, 16, 4, 4, "Holberton")


class TestSquare_size(unittest.TestCase):
    """Unittests for testing instantiation of the Square size attribute."""

    def test_size_none(self):
        with self.assertRaises(TypeError):
            Square(None)

    def test_size_none_2(self):
        with self.assertRaises(TypeError):
            Square(None, 6, 7)

    def test_size_float(self):
        with self.assertRaises(TypeError):
            Square(5.0, 32, 63, 554.0)

    def test_size_n(self):
        with self.assertRaises(ValueError):
            Square(-75, 52, 53, 543)

    def test_size_string(self):
        with self.assertRaises(TypeError):
            Square("Hello", 52, 53, 543)

    def test_size_zero(self):
        with self.assertRaises(ValueError):
            Square(0, 52, 53, 543)

    def test_size_float_inf(self):
        with self.assertRaises(TypeError):
            Square(float('inf'), 52, 53, 543)

    def test_size_float_nan(self):
        with self.assertRaises(TypeError):
            Square(float('nan'), 52, 53, 543)

    def test_size_complex(self):
        with self.assertRaises(TypeError):
            Square(complex(5), 52, 53, 543)


class TestSquare_x(unittest.TestCase):
    """Unittests for testing instantiation of the Square x attribute."""

    def test_x_none(self):
        with self.assertRaises(TypeError):
            Square(x=None)

    def test_x_none_2(self):
        with self.assertRaises(TypeError):
            Square(4, None, 7)

    def test_x_float(self):
        with self.assertRaises(TypeError):
            Square(5, 32.43, 63)

    def test_x_n(self):
        with self.assertRaises(ValueError):
            Square(75, -52, 53, 543)

    def test_x_string(self):
        with self.assertRaises(TypeError):
            Square(4, "Betty", 53, 543)

    def test_x_float_inf(self):
        with self.assertRaises(TypeError):
            Square(4, float('inf'), 53, 543)

    def test_x_float_nan(self):
        with self.assertRaises(TypeError):
            Square(97, float('nan'), 53, 543)

    def test_x_complex(self):
        with self.assertRaises(TypeError):
            Square(5, complex(5), 53, 543)


class TestSquare_y(unittest.TestCase):
    """Unittests for testing instantiation of the Square y attribute."""

    def test_y_none(self):
        with self.assertRaises(TypeError):
            Square(y=None)

    def test_y_none_2(self):
        with self.assertRaises(TypeError):
            Square(4, 5, None, 7)

    def test_y_float(self):
        with self.assertRaises(TypeError):
            Square(5, 4, 32.43, 4)

    def test_y_n(self):
        with self.assertRaises(ValueError):
            Square(75, 54, -52, 543)

    def test_y_string(self):
        with self.assertRaises(TypeError):
            Square(4, 6, "Betty", 543)

    def test_y_float_inf(self):
        with self.assertRaises(TypeError):
            Square(4, 36, float('inf'), 543)

    def test_y_float_nan(self):
        with self.assertRaises(TypeError):
            Square(97, 51, float('nan'), 543)

    def test_y_complex(self):
        with self.assertRaises(TypeError):
            Square(5, 75, complex(5), 543)


class TestSquare_id(unittest.TestCase):
    """Unittests for testing instantiation of the Square id attribute."""

    def test_id_none(self):
        with self.assertRaises(TypeError):
            Square(id=None)

    def test_id_float(self):
        s = Square(5, 4, 5, 32.43)
        self.assertEqual(32.43, s.id)

    def test_id_n(self):
        s = Square(75, 54, 32, -52)
        self.assertEqual(-52, s.id)

    def test_id_float_inf(self):
        s = Square(4, 36, 434, float('inf'))
        self.assertEqual(float('inf'), s.id)

    def test_id_complex(self):
        s = Square(5, 75, 434, complex(5))
        self.assertEqual(complex(5), s.id)


class TestSquare_order_of_initialization(unittest.TestCase):
    """Unittests for testing order of Square attribute initialization."""

    def test_size_before_x(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("invalid size", "invalid x")

    def test_size_before_y(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("invalid size", 1, "invalid y")

    def test_x_before_y(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "invalid x", "invalid y")


class TestSquare_area(unittest.TestCase):
    """Unittests for testing the area method of the Square class."""

    def test_area_small(self):
        self.assertEqual(100, Square(10, 0, 0, 1).area())

    def test_area_large(self):
        s = Square(999999999999999999, 0, 0, 1)
        self.assertEqual(999999999999999998000000000000000001, s.area())

    def test_area_changed_attributes(self):
        s = Square(2, 0, 0, 1)
        s.size = 7
        self.assertEqual(49, s.area())

    def test_area_changed_number_n(self):
        s = Square(2, 0, 0, 1)
        with self.assertRaises(TypeError):
            s.area(None, 5)

    def test_area_one_arg(self):
        s = Square(2, 10, 1, 1)
        with self.assertRaises(TypeError):
            s.area(1)

    def test_area_one_complex_arg(self):
        s = Square(2, 10, 1, 1)
        with self.assertRaises(TypeError):
            s.area(1, complex(5))

    def test_area_one_complex_arg_2(self):
        s = Square(2, 10, 1, 1)
        with self.assertRaises(TypeError):
            s.area(complex(41), 5)

    def test_area_one_complex_arg_2(self):
        s = Square(2, 10, 1, 1)
        with self.assertRaises(TypeError):
            s.area(4, "Holberton")


class TestSquare_stdout(unittest.TestCase):
    """Unittests for testing __str__ and display methods of Square class."""

    @staticmethod
    def capture_stdout(sq, method):
        """Captures and returns text printed to stdout.
        Args:
            sq (Square): The Square ot print to stdout.
            method (str): The method to run on sq.
        Returns:
            The text printed to stdout by calling method on sq.
        """
        capture = io.StringIO()
        sys.stdout = capture
        if method == "print":
            print(sq)
        else:
            sq.display()
        sys.stdout = sys.__stdout__
        return capture

    def test_print_size(self):
        s = Square(4)
        capture = TestSquare_stdout.capture_stdout(s, "print")
        correct = "[Square] ({}) 0/0 - 4\n".format(s.id)
        self.assertEqual(correct, capture.getvalue())

    def test_size_x(self):
        s = Square(5, 43)
        correct = "[Square] ({}) 43/0 - 5".format(s.id)
        self.assertEqual(correct, s.__str__())

    def test_size_x_y(self):
        s = Square(7, 4, 22)
        correct = "[Square] ({}) 4/22 - 7".format(s.id)
        self.assertEqual(correct, str(s))

    def test_size_x_y_id(self):
        s = Square(2, 88, 4, 19)
        self.assertEqual("[Square] (19) 88/4 - 2", str(s))

    def test_changed_attributes(self):
        s = Square(7, 5, 34, [4])
        s.size = 15
        s.x = 8
        s.y = 10
        self.assertEqual("[Square] ([4]) 8/10 - 15", str(s))

    def test_str_method_one_arg(self):
        s = Square(1, 2, 3, 4)
        with self.assertRaises(TypeError):
            s.__str__(1)

    # Test display method
    def test_display_size(self):
        s = Square(2, 2, 0, 53)
        capture = TestSquare_stdout.capture_stdout(s, "display")
        self.assertEqual("  ##\n  ##\n", capture.getvalue())

    def test_display_size_x(self):
        s = Square(4, 1, 0, 18)
        capture = TestSquare_stdout.capture_stdout(s, "display")
        self.assertEqual(" ####\n ####\n ####\n ####\n", capture.getvalue())

    def test_display_size_y(self):
        s = Square(4, 0, 1, 12)
        capture = TestSquare_stdout.capture_stdout(s, "display")
        display = "\n####\n####\n####\n####\n"
        self.assertEqual(display, capture.getvalue())

    def test_display_size_x_y(self):
        s = Square(2, 3, 2, 1)
        capture = TestSquare_stdout.capture_stdout(s, "display")
        display = "\n\n   ##\n   ##\n"
        self.assertEqual(display, capture.getvalue())

    def test_display_one_arg(self):
        s = Square(3, 4, 5, 2)
        with self.assertRaises(TypeError):
            s.display(1)


class TestSquare_update_args(unittest.TestCase):
    """Unittests for testing update args method of the Square class."""

    def test_update_args_zero(self):
        s = Square(10, 10, 10, 10)
        s.update()
        self.assertEqual("[Square] (10) 10/10 - 10", str(s))

    def test_update_one_arg(self):
        s = Square(10, 10, 10, 10)
        s.update(13)
        self.assertEqual("[Square] (13) 10/10 - 10", str(s))

    def test_update_x_arg(self):
        s = Square(10, 3, 10, 10)
        s.update(x=13)
        self.assertEqual("[Square] (10) 13/10 - 10", str(s))

    def test_update_y_arg(self):
        s = Square(10, 10, 3, 4)
        s.update(13)
        s.y = 53
        s.update(5)
        self.assertEqual("[Square] (5) 10/53 - 10", str(s))

    def test_update_args_two(self):
        s = Square(10, 10, 10, 10)
        s.update(89, 2)
        self.assertEqual("[Square] (89) 10/10 - 2", str(s))

    def test_update_args_three(self):
        s = Square(10, 10, 10, 10)
        s.update(89, 2, 3)
        self.assertEqual("[Square] (89) 3/10 - 2", str(s))

    def test_update_args_four(self):
        s = Square(10, 10, 10, 10)
        s.update(89, 2, 3, 4)
        self.assertEqual("[Square] (89) 3/4 - 2", str(s))

    def test_update_args_more_than_four(self):
        s = Square(10, 10, 10, 10)
        s.update(89, 2, 3, 4, 5)
        self.assertEqual("[Square] (89) 3/4 - 2", str(s))

    def test_update_args_width_setter(self):
        s = Square(10, 10, 10, 10)
        s.update(89, 2)
        self.assertEqual(2, s.width)

    def test_update_args_height_setter(self):
        s = Square(10, 10, 10, 10)
        s.update(89, 2)
        self.assertEqual(2, s.height)

    def test_update_args_none_id(self):
        s = Square(10, 10, 10, 10)
        s.update(None)
        correct = "[Square] ({}) 10/10 - 10".format(s.id)
        self.assertEqual(correct, str(s))

    def test_update_args_None_id_and_more(self):
        s = Square(10, 10, 10, 10)
        s.update(None, 4, 5)
        correct = "[Square] ({}) 5/10 - 4".format(s.id)
        self.assertEqual(correct, str(s))

    def test_update_args_twice(self):
        s = Square(10, 10, 10, 10)
        s.update(89, 2, 3, 4)
        s.update(4, 3, 2, 89)
        self.assertEqual("[Square] (4) 2/89 - 3", str(s))

    def test_update_args_invalid_size_type(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(89, "invalid")

    def test_update_args_size_zero(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(89, 0)

    def test_update_args_size_negative(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(89, -4)

    def test_update_args_invalid_x(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s.update(89, 1, "invalid")

    def test_update_args_x_negative(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s.update(98, 1, -4)

    def test_update_args_invalid_y(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s.update(89, 1, 2, "invalid")

    def test_update_args_y_negative(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s.update(98, 1, 2, -4)

    def test_update_args_size_before_x(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(89, "invalid", "invalid")

    def test_update_args_size_before_y(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(89, "invalid", 2, "invalid")

    def test_update_args_x_before_y(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s.update(89, 1, "invalid", "invalid")


class TestSquare_update_kwargs(unittest.TestCase):
    """Unittests for testing update kwargs method of Square class."""

    def test_update_kwargs_one(self):
        s = Square(10, 10, 10, 10)
        s.update(id=1)
        self.assertEqual("[Square] (1) 10/10 - 10", str(s))

    def test_update_kwargs_two(self):
        s = Square(10, 10, 10, 10)
        s.update(size=1, id=2)
        self.assertEqual("[Square] (2) 10/10 - 1", str(s))

    def test_update_kwargs_three(self):
        s = Square(10, 10, 10, 10)
        s.update(y=1, size=3, id=89)
        self.assertEqual("[Square] (89) 10/1 - 3", str(s))

    def test_update_kwargs_four(self):
        s = Square(10, 10, 10, 10)
        s.update(id=89, x=1, y=3, size=4)
        self.assertEqual("[Square] (89) 1/3 - 4", str(s))

    def test_update_kwargs_width_setter(self):
        s = Square(10, 10, 10, 10)
        s.update(id=89, size=8)
        self.assertEqual(8, s.width)

    def test_update_kwargs_height_setter(self):
        s = Square(10, 10, 10, 10)
        s.update(id=89, size=9)
        self.assertEqual(9, s.height)

    def test_update_kwargs_None_id(self):
        s = Square(10, 10, 10, 10)
        s.update(id=None)
        correct = "[Square] ({}) 10/10 - 10".format(s.id)
        self.assertEqual(correct, str(s))

    def test_update_kwargs_None_id_and_more(self):
        s = Square(10, 10, 10, 10)
        s.update(id=None, size=7, x=18)
        correct = "[Square] ({}) 18/10 - 7".format(s.id)
        self.assertEqual(correct, str(s))

    def test_update_kwargs_twice(self):
        s = Square(10, 10, 10, 10)
        s.update(id=89, x=1)
        s.update(y=3, x=15, size=2)
        self.assertEqual("[Square] (89) 15/3 - 2", str(s))

    def test_update_kwargs_invalid_size(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(size="invalid")

    def test_update_kwargs_size_zero(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(size=0)

    def test_update_kwargs_size_negative(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(size=-3)

    def test_update_kwargs_invalid_x(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s.update(x="invalid")

    def test_update_kwargs_x_negative(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s.update(x=-5)

    def test_update_kwargs_invalid_y(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s.update(y="invalid")


class TestSquare_to_dictionary(unittest.TestCase):
    """Unittests for testing to_dictionary method of the Square class."""

    def test_to_dictionary_output(self):
        s = Square(10, 2, 1, 1)
        correct = {'id': 1, 'x': 2, 'size': 10, 'y': 1}
        self.assertDictEqual(correct, s.to_dictionary())

    def test_to_dictionary_no_object_changes(self):
        s1 = Square(10, 2, 1, 2)
        s2 = Square(1, 2, 10)
        s2.update(**s1.to_dictionary())
        self.assertNotEqual(s1, s2)

    def test_to_dictionary_arg(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaises(TypeError):
            s.to_dictionary(1)


if __name__ == "__main__":
    unittest.main()
