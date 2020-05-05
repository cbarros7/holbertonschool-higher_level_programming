#!/usr/bin/python3


def multiple_returns(sentence):
    count = len(sentence)
    if count == 0:
        return None
    else:
        first = sentence[0]
        return count, first
