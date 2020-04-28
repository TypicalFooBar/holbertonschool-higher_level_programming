#!/usr/bin/python3


def copy_list(l):
    newList = None
    newList = [[col for col in row] for row in l]
    return newList
