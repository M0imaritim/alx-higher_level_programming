#!/usr/bin/python3
def no_c(my_string):
    if my_string is None:
        return
    new_str = list(my_string)
    for i in new_str:
        if i == 'c' and i == 'C':
            new_str.remove(i)
    return ''.join(new_str)
