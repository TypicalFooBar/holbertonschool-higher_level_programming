#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    aSize = len(tuple_a)
    bSize = len(tuple_b)
    minSize = min(aSize, bSize)
    sumTuple = [0] * minSize



    for i in range(minSize):
        sumTuple[i] += tuple_a[i]

    for i in range(minSize):
        sumTuple[i] += tuple_b[i]

    return tuple(sumTuple)
