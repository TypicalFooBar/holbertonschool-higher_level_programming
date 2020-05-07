#!/usr/bin/python3
"""Doc"""

class Base:
    """Doc"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Doc"""
        self.id = self.__nb_objects + 1

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1