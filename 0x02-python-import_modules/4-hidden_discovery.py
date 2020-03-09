#!/usr/bin/python3

import hidden4

def main():
    names = dir(hidden4)
    for name in names:
        if not name.startswith("__"):
            print(name)


if __name__ == "__main__":
    main()
