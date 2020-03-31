#!/usr/bin/python3
def roman_to_int(roman_string):
    sum = 0
    lastRoman = None

    if isinstance(roman_string, str):
        for c in roman_string:
            if c is 'I':
                sum += 1
            elif c is 'V':
                if lastRoman is 'I':
                    sum += 3
                else:
                    sum += 5
            elif c is 'X':
                if lastRoman is 'I':
                    sum += 8
                else:
                    sum += 10
            elif c is 'L':
                sum += 50
            elif c is 'C':
                if lastRoman is 'X':
                    sum += 80
                else:
                    sum += 100
            elif c is 'D':
                sum += 500
            
            lastRoman = c

    return sum
