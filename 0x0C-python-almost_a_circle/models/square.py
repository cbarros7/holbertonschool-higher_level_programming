#!/usr/bin/python3
# square.py
# Carlos Barros <1543@holbertonschool.com>
"""Define Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square: Class define square

    Args:
        Rectangle (class): parent class
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """__str__ print information for square

        Returns:
            [str]: [Square] (<id>) <x>/<y> - <size>
        """
        return '[Square] ({}) {}/{} - {}'.format(self.id, self.x,
                                                 self.y, self.width)

    @property
    def size(self):
        """Getter value for size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter value for size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update use args and kwargs"""
        if args and args != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        super().__init__(self.width,
                                         self.height, self.x,
                                         self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1
        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        super().__init__(self.width,
                                         self.height, self.x,
                                         self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Dictionary with values for rectangle"""
        return {"id": self.id, "size": self.size,
                "x": self.x, "y": self.y}
