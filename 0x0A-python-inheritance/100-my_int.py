#!/usr/bin/python3


class MyInt(int):
    """MyInt"""

    def __eq__(self, other):
        return self != other

    def __ne__(self, other):
        return self == other
