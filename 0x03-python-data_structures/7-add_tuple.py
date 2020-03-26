#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    sumTuple = [0, 0]

    aSize = len(tuple_a)
    bSize = len(tuple_b)



    for i in range(aSize):
        sumTuple[i] += tuple_a[i]

    for i in range(bSize):
        sumTuple[i] += tuple_b[i]

    return (sumTuple[0], sumTuple[1])
