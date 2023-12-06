#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    newlist = sorted(list(a_dictionary.items()))
    for key, value in newlist:
        print("{}: {}".format(key, value))
