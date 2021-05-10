#!/usr/bin/python3
"""
Create a locked class
wherein the only malleable
variable is first_name
"""


class LockedClass():
    """ Class Doc """
    __slots__ = 'first_name'
