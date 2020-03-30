#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    newMatrix = [row[:] for row in matrix]

    for row in range(len(newMatrix)):
        for col in range(len(newMatrix[row])):
            newMatrix[row][col] = newMatrix[row][col] ** 2

    return newMatrix
