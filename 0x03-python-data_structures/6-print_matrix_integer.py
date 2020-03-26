#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        isFirstInRow = True
        for col in row:
            if not isFirstInRow:
                print(" ", end="")
            print("{:d}".format(col), end="")
            isFirstInRow = False
        print("")
