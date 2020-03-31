#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    newDictionary = {}

    for key in a_dictionary:
        newDictionary[key] = a_dictionary[key] * 2

    return newDictionary
