#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    # newMatrix = [row[:] for row in matrix]

    # for row in range(len(newMatrix)):
    #     for col in range(len(newMatrix[row])):
    #         newMatrix[row][col] = newMatrix[row][col] ** 2

    # return newMatrix

    newMatrix = [[col**2 for col in row] for row in matrix]
    return newMatrix
