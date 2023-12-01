#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    newlist = [i for i in my_list]
    length = len(newlist)
    if idx >= length or idx < 0:
        return None
    newlist[idx] = element
    return newlist
