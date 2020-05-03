#!/usr/bin/python3


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square"""

    def __init__(self, size):
        self.integer_validator("size", size)

        self._size = size

    def area(self):
        return self._size * self._size
