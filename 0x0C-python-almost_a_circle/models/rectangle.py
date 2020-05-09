#!/usr/bin/python3
"""Description"""


from .base import Base


class Rectangle(Base):
    """Description"""

    __width = 0
    __height = 0
    __x = 0
    __y = 0

    def __init__(self, width, height, x=0, y=0, id=None):
        """Description"""
        super(Rectangle, self).__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Description"""
        return self.__width

    @width.setter
    def width(self, value):
        """Description"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Description"""
        return self.__height

    @height.setter
    def height(self, value):
        """Description"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Description"""
        return self.__x

    @x.setter
    def x(self, value):
        """Description"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Description"""
        return self.__y

    @y.setter
    def y(self, value):
        """Description"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Description"""
        return self.width * self.height

    def display(self):
        """Description"""
        # Print empty rows for each column
        for _ in range(self.y):
            print()

        for _ in range(self.height):
            # Print space ahead of each row
            for _ in range(self.x):
                print(" ", end="")
            # Print this row for the square
            for _ in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """Description"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """Description"""
        if args is not None:
            try:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
            except IndexError:
                # We've updated all we could and hit one that was
                # not included because it was out of range
                pass
        else:
            for key, value in kwargs:
                if key == "id":
                    self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value
