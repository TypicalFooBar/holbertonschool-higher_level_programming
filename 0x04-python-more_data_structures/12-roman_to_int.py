#!/usr/bin/python3
def roman_to_int(roman_string):
    sum = 0
    lastCharWasI = False

    for c in roman_string:
        if c is 'I':
            sum += 1
            lastCharWasI = True
        elif c is 'V':
            if lastCharWasI:
                sum += 3
            else:
                sum += 5

            lastCharWasI = False
        elif c is 'X':
            sum += 10
            lastCharWasI = False
        elif c is 'L':
            sum += 50
            lastCharWasI = False
        elif c is 'C':
            sum += 100
            lastCharWasI = False
        elif c is 'D':
            sum += 500
            lastCharWasI = False

    return sum
