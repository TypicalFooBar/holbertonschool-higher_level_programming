#!/usr/bin/python3
import sys


def main():
    argc = len(sys.argv) - 1

    if argc == 0:
        print("0 arguments.")
    elif argc == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(argc))

    if argc > 0:
        for i in range(len(sys.argv)):
            if i == 0:
                continue
            else:
                print("{}: {}".format(i, sys.argv[i]))

if __name__ == "__main__":
    main()
