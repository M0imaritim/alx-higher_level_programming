#!/usr/bin/python3
def no_c(my_string):
    if my_string is None:
        return
    new_str = ''
    for i in my_string:
        if i != 'c' and i != 'C':
            new_str += i
    return new_str
