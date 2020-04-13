#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    numberPrinted = 0

    try:
        for i in range(x):
            print("{}".format(my_list[i]), end="")
            numberPrinted += 1
    except:
        print("")
        return numberPrinted
    
    print("")
    return numberPrinted