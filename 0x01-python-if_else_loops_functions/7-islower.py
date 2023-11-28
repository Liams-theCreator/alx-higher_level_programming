#!/usr/bin/python3
def islower(c):
    for a in range(ord('a'), ord('z')):
        if c == chr(a):
            return True
    return False
