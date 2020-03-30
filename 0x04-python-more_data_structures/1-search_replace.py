#!/usr/bin/python3


def search_replace(my_list, search, replace):
    newMatrix = [row[:] for row in matrix]

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            newMatrix[row][col] = newMatrix[row][col] ** 2

    return newMatrix
