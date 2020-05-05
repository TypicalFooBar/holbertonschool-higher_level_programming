#!/usr/bin/python3


def number_of_lines(filename=""):
    i = 0

    with open(filename) as f:
        atLeastOneLine = False

        for i, line in enumerate(f):
            atLeastOneLine = True

        # Account for index starting at zero
        if atLeastOneLine:
            i += 1

    return i
