#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    numberPrinted = 0

    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            numberPrinted += 1
        except IndexError as ex:
            print(ex)
        except:
            None

    print()
    return numberPrinted
