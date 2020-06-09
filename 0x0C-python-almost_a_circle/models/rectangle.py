#!/usr/bin/python3
# rectangle.py
# Carlos Barros <1543@holbertonschool.com>
"""Define Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Rectangle: Class define rectangle

    Args:
        Base (class): parent class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """__init__ initialized constuctor

        Args:
            width (int)
            height (int)
            x (int, optional): Defaults to 0.
            y (int, optional): Defaults to 0.
            id ([type], optional): Defaults to None.
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Getter value for width"""
        return self.__width

    @width.setter
    def width(self, width):
        """Setter value for width"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """Getter value for height"""
        return self.__height

    @height.setter
    def height(self, height):
        """Setter value for height"""
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """Getter value for x"""
        return self.__x

    @x.setter
    def x(self, x):
        """Setter value for x"""
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """Getter value for y"""
        return self.__y

    @y.setter
    def y(self, y):
        """Setter value for y"""
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """area: area rectangle

        Returns:
            int: area
        """
        return self.width * self.height

    def display(self):
        """display: prints in stdout the Rectangle instance
        with the character #
        """
        for row in range(self.y):
            print("")

        for col in range(self.height):
            for k in range(self.x):
                print(" ", end="")
            for j in range(self.width):
                print("#", end="")
            print("")

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
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
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
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Dictionary with values for rectangle"""
        return {"id": self.id, "width": self.width,
                "height": self.height, "x": self.x,
                "y": self.y}

    def __str__(self):
        """__str__ print information for rectangle

        Returns:
            [str]: [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return '[Rectangle] ({}) {}/{} - {}/{}'.format(self.id, self.x,
                                                       self.y, self.width,
                                                       self.height)
