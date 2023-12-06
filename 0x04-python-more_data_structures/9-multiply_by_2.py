#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    newdictio = dict()
    for name, value in a_dictionary:
        val = value * 2
        newdictio[name] = val
    return newdictio
