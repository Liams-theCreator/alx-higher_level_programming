#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is None:
        return None
    tupile = (len(sentence), sentence[0])
    return tupile
