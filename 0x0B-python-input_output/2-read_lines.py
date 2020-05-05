#!/usr/bin/python3


def read_lines(filename="", nb_lines=0):
    lineData = ""

    with open(filename) as f:
        if (nb_lines <= 0):
            lineData = f.read()
        else:
            for i, line in enumerate(f):
                if i < nb_lines:
                    lineData += line
                else:
                    break

    f.close()
    print(lineData, end="")
