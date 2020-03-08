#!/usr/bin/python3

usedCombinations = [[0 for i in range(10)] for j in range(10)]

for i in range(0, 10):
    for j in range(0, 10):
        if i == j:
            usedCombinations[i][j] = 1
            usedCombinations[j][i] = 1
            continue

        if usedCombinations[i][j] == 1 or usedCombinations[j][i] == 1:
            continue

        print("{}{}".format(i, j), end='')

        # Mark this combination as used
        usedCombinations[i][j] = 1
        usedCombinations[j][i] = 1

        if i == 8 and j == 9:
            print("")
            break

        # Print a comma
        print(", ", end='')
