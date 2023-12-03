#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is "":
        return (0, None)
    tupile = (len(sentence), sentence[0])
    return tupile
