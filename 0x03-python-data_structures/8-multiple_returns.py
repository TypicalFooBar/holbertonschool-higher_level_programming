#!/usr/bin/python3


def multiple_returns(sentence):
    if sentence is None:
        return None

    length = len(sentence)

    if length is 0:
        return (length, None)

    return (length, sentence[0])
