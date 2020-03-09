#!/usr/bin/python3

isLower = True
lowerOffset = 32
valueToPrint = 0

for i in reversed(range(97, 123)):
    if isLower:
        valueToPrint = i
        isLower = False
    else:
        valueToPrint = i - lowerOffset
        isLower = True

    print("{}".format(chr(valueToPrint)), end='')
