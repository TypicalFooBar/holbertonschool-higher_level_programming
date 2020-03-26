#!/usr/bin/python3


def multiple_returns(sentence):
    if sentence is None:
        return None

    length = len(sentence)

    if length is 0:
        return None

    return (length, sentence[0])
