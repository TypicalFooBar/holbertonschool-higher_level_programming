#!/usr/bin/python3


class MyInt(int):
    """MyInt"""

    def __eq__(self, other):
        return other.__ne__(self)

    def __ne__(self, other):
        return other.__eq__(self)
