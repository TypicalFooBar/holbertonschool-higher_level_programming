#!/usr/bin/python3


def validateMatrixAndGetRowSize(matrix):
    nonList = "matrix must be a matrix (list of lists) of integers/floats"
    wrongSizeRow = "Each row of the matrix must have the same size"
    rowSize = -1

    if (
        not isinstance(matrix, list)
    ):
        raise TypeError(nonList)
    else:
        for row in matrix:
            # Make sure this is a row
            if not isinstance(row, list):
                raise TypeError(nonList)

            # Get the length of the row
            if rowSize == -1:
                rowSize = len(row)
            # Make sure all rows are the same length
            elif len(row) != rowSize:
                raise TypeError(wrongSizeRow)

            # Make sure each element is an int or float
            for col in row:
                if (
                    not isinstance(col, int) and
                    not isinstance(col, float)
                ):
                    raise TypeError(nonList)


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
