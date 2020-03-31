#!/usr/bin/python3
def roman_to_int(roman_string):
    sum = 0
    lastCharWasI = False

    if isinstance(roman_string, str):
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
                if lastCharWasI:
                    sum += 8
                else:
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
