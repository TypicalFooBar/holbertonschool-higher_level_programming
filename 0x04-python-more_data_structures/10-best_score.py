#!/usr/bin/python3


def best_score(a_dictionary):
    bestScore = None
    bestScoreKey = None

    if a_dictionary is None:
        return None

    for key in a_dictionary:
        if bestScore is None or a_dictionary[key] > bestScore:
            bestScore = a_dictionary[key]
            bestScoreKey = key

    return bestScoreKey
