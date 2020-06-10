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


        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def __str__(self):
        """__str__ print information for rectangle

        Returns:
            [str]: [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return '[Rectangle] ({}) {}/{} - {}/{}'.format(self.id, self.x,
                                                       self.y, self.width,
                                                       self.height)

    @property
    def width(self):
        """Getter value for width"""
        return self.__width

    @width.setter
    def width(self, value):
        self.integer_validator("width", value)
        self.__width = value

    @property
    def height(self):
        """Property height: height of rectangle
        setter validates value is an integer > 0
        Parameter:
            value: value of the width
        Raises:
            TypeError: if value is not an integer
            ValueError: if value is <= 0
        """
        return self.__height

    @height.setter
    def height(self, value):
        self.integer_validator("height", value)
        self.__height = value

    @property
    def x(self):
        """Property x: x position of rectangle
        setter validates value is an integer >= 0
        Parameter:
            value: value of the width
        Raises:
            TypeError: if value is not an integer
            ValueError: if value is < 0
        """
        return self.__x

    @x.setter
    def x(self, value):
        self.integer_validator("x", value)
        self.__x = value

    @property
    def y(self):
        """Property y: y position of rectangle
        setter validates value is an integer >= 0
        Parameter:
            value: value of the width
        Raises:
            TypeError: if value is not an integer
            ValueError: if value is < 0
        """
        return self.__y

    @y.setter
    def y(self, value):
        self.integer_validator("y", value)
        self.__y = value

    def integer_validator(self, name, value):
        """Validates a given value is a postive int
        Parameters:
            name: name of variable to validate
            value: value to validate
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if (name == "width" or name == "height") and value <= 0:
            raise ValueError("{} must be > 0".format(name))
        if (name == "x" or name == "y") and value < 0:
            raise ValueError("{} must be >= 0".format(name))

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
                        super().__init__(self.width, self.height,
                                         self.x, self.y)
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
        return {"id": self.id, "width": self.width, "height": self.height,
                "x": self.x, "y": self.y}
