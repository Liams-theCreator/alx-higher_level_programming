#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list is None:
        return None
    sum = 0
    newlist = set()
    for i in my_list:
        newlist.add(i)
    for nums in newlist:
        sum += nums
    return nums
