#!/usr/bin/python3


def add_attribute(obj, key, value):
    setattr(obj, key, value)
    if not hasattr(obj, key):
        raise TypeError("can't add new attribute")