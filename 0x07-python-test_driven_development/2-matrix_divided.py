#!/usr/bin/python3


def validateMatrixAndGetRowSize(matrix):
    nonListMessage = "matrix must be a matrix (list of lists) of integers/floats"
    wrongSizeRowMessage = "Each row of the matrix must have the same size"
    rowSize = -1

    if (
        not isinstance(matrix, list)
    ):
        raise TypeError(nonListMessage)
    else:
        for row in matrix:
            # Make sure this is a row
            if not isinstance(row, list):
                raise TypeError(nonListMessage)

            # Get the length of the row
            if rowSize == -1:
                rowSize = len(row)
            # Make sure all rows are the same length
            elif len(row) != rowSize:
                raise TypeError(wrongSizeRowMessage)

def validateDivisor(div):
    if (
        not isinstance(div, int) and
        not isinstance(div, float)
    ):
        raise TypeError("div must be a number")
    elif div == 0:
        raise TypeError("division by zero")

def matrix_divided(matrix, div):
    validateDivisor(div)
    validateMatrixAndGetRowSize(matrix)

    newMatrix = [[round(col/div, 2) for col in row] for row in matrix]
    return newMatrix
