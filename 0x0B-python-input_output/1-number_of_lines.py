#!/usr/bin/python3


def number_of_lines(filename=""):
    with open(filename) as f:
        for i, line in enumerate(f):
            pass

    return i + 1
