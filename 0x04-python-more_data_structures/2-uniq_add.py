#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list is None:
        return
    result = 0
    n_list = set(my_list)

    for i in n_list:
        result += i
    return result
