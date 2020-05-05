#!/usr/bin/python3


def number_of_lines(filename=""):
    i = 0

    with open(filename) as f:
        for i, line in enumerate(f):
            pass

    return i
