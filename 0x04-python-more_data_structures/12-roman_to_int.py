#!/usr/bin/python3
def roman_to_int(roman_string):
    summ = 0
    if not isinstance(roman_string,str) or roman_string is None:
        return 0
    dict = {'I': 1, 'IV': 4, 'V': 5, 'VI': 6, 'VII': 7, 'VIII': 8, 'IX':9,
            'X':10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    lis = [dict[char] for char in roman_string if char in dict]
    for i in lis:
        summ += i
    return summ
