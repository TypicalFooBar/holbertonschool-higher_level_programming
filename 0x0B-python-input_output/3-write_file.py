#!/usr/bin/python3


def write_file(filename="", text=""):
    with open(filename) as f:
        f.write(text)

    f.close()
    print(len(text), end="")
