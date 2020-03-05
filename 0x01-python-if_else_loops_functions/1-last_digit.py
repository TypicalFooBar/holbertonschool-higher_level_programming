#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

isNegative = number < 0
lastDigit = abs(number) % 10

print("Last digit of {} is {} and is {}".format(
    number,
    lastDigit,
    "less than 6 and not 0" if isNegative else
    ("0" if lastDigit == 0 else "greater than 5")
))
