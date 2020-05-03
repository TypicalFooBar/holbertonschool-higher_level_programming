#!/usr/bin/python3


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle"""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self._width = width
        self._height = height

    def area(self):
        return self._width * self._height

    def __str__(self):
        return "[Rectangle] {}/{}".format(self._width, self._height)

    def print(self):
        return self.__str__()
