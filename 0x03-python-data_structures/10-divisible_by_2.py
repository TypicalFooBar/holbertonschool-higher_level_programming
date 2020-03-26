#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    listLength = len(my_list)
    divisibleBy2List = [False] * listLength

    for i in range(listLength):
        if my_list[i] % 2 is 0:
            divisibleBy2List[i] = True

    return divisibleBy2List
