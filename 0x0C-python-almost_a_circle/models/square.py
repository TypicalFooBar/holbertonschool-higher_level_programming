#!/usr/bin/python3
"""Description"""


from .rectangle import Rectangle


class Square(Rectangle):
    """Description"""

    def __init__(self, size, x=0, y=0, id=None):
        """Description"""
        super(Square, self).__init__(size, size, x, y, id)

    def __str__(self):
        """Description"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)
