#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    aSize = len(tuple_a)
    bSize = len(tuple_b)
    maxSize = max(aSize, bSize)
    sumTuple = [0] * maxSize



    for i in range(aSize):
        sumTuple[i] += tuple_a[i]

    for i in range(bSize):
        sumTuple[i] += tuple_b[i]

    return tuple(sumTuple)
