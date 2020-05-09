#!/usr/bin/python3
"""Description"""


import json


class Base:
    """Description"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Description"""
        self.id = self.__nb_objects + 1

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1

    @staticmethod
    def to_json_string(list_dictionaries):
        """Descriptions"""
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
