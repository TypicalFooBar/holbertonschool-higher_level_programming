#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    newMatrix = [row[:] for row in matrix]

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            newMatrix[row][col] = newMatrix[row][col] ** 2

    return newMatrix
