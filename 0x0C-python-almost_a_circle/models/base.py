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

    @classmethod
    def save_to_file(cls, list_objs):
        """Description"""
        jsonText = "[]"

        if list_objs is not None:
            jsonObjects = []

            for obj in list_objs:
                jsonObjects.append(cls.to_dictionary(obj))

            jsonText = cls.to_json_string(jsonObjects)

        with open("{}.json".format(cls.__name__), "w") as f:
            f.write(jsonText)
        f.close()

    @staticmethod
    def from_json_string(json_string):
        """Description"""
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            new = cls(1, 1)
        elif cls.__name__ == "Square":
            new = cls(1)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        filename = "{}.json".format(cls.__name__)
        jsonString = ""

        try:
            with open(filename, "r") as f:
                jsonString = f.read()
        except:
            jsonString = "[]"

        jsonObjectList = cls.from_json_string(jsonString)

        objList = []
        for item in jsonObjectList:
            objList.append(cls.create(**item))

        return objList
