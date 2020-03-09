#!/usr/bin/python3
import sys


def main():
    total = 0

    for i in range(len(sys.argv)):
        if i == 0:
            continue
        else:
            total += int(sys.argv[i])

    print("{}".format(total))

if __name__ == "__main__":
    main()
