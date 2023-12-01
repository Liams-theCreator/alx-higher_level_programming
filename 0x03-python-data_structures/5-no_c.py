#!/usr/bin/python3
def no_c(my_string):
    if my_string == []:
        return None
    newstr = ""
    for i in my_string:
        if i == "c" or i == 'C':
            continue
        else:
            newstr += i
    return newstr
