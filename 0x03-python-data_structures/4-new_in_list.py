#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list
    list_n = my_list.copy()
    list_n[idx] = element
    return list_n
