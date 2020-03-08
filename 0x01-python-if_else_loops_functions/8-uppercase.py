#!/usr/bin/python3
def uppercase(str):
    uppercaseOffset = 32
    offset = 0

    for c in str:
        # First, set the offset
        if ord(c) in range(97, 123):
            offset = uppercaseOffset
        else:
            offset = 0

        # Print the uppercase ascii character
        print(chr(ord(c) - offset), end='')

    # Print a new line
    print()
