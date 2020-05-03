#!/usr/bin/python3


BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """Rectangle"""

    _width = 0
    _height = 0

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self._width = width
        self._height = height
