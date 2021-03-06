#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv


def main():
    argc = len(argv) - 1
    firstInt = 0
    secondInt = 0
    operator = '+'
    result = 0

    if argc != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    firstInt = int(argv[1])
    operator = argv[2]
    secondInt = int(argv[3])

    if operator == '+':
        result = add(firstInt, secondInt)
    elif operator == '-':
        result = sub(firstInt, secondInt)
    elif operator == '*':
        result = mul(firstInt, secondInt)
    elif operator == '/':
        result = div(firstInt, secondInt)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    print("{} {} {} = {}".format(firstInt, operator, secondInt, result))

if __name__ == "__main__":
    main()
