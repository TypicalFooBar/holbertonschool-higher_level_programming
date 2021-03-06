#!/usr/bin/python3


class Student:
    first_name = ""
    last_name = ""
    age = ""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        else:
            studentAttrs = {}
            for item in attrs:
                try:
                    studentAttrs[item] = self.__dict__[item]
                except KeyError:
                    # Do nothing if the key did not exist
                    pass

            return studentAttrs
