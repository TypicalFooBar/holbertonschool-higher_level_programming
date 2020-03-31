#!/usr/bin/python3


def best_score(a_dictionary):
    bestScore = None

    if a_dictionary == None:
        return None

    for key in a_dictionary:
        if bestScore is None or a_dictionary[key] > bestScore:
            bestScore = a_dictionary[key]

    return bestScore
