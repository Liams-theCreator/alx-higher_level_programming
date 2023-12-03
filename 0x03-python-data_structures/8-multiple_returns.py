#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is None:
        return None
    length = len(sentence)
    tupile = (length, sentence[0])
    return tupile
