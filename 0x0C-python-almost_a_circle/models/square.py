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

    @property
    def size(self):
        """Description"""
        return self.width

    @size.setter
    def size(self, value):
        """Description"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Description"""
        if args is not None and len(args) > 0:
            try:
                self.id = args[0]
                self.width = args[1]
                self.height = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                # We've updated all we could and hit one that was
                # not included because it was out of range
                pass
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.width = value
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value
