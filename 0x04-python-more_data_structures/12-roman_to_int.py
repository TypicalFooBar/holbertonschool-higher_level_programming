#!/usr/bin/python3
def roman_to_int(roman_string):
    sum = 0

    for c in roman_string:
        if c is 'I':
            sum += 1
        elif c is 'V':
            sum += 5
        elif c is 'X':
            sum += 10
        elif c is 'L':
            sum += 50
        elif c is 'C':
            sum += 100
        elif c is 'D':
            sum += 500

    return sum
