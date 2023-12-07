#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0
    romania = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
               'C': 100, 'D': 500, 'M': 1000}
    newin = 0
    prev = 0
    for i in roman_string:
        current = romania[i]
        if current > prev:
            newin += current - 1 * prev
        else:
            newin += current
        prev = current
    return newin
