#!/usr/bin/python3
def magic_string(h="Holberton"):
    magic_string.s=magic_string.s+', '+h if hasattr(magic_string, "s") else h
    return magic_string.s