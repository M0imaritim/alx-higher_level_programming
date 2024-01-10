#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list is None or search is None or replace is None:
        return
    n_list = my_list.copy()
    n_list = [replace if element == search else element for element in my_list]
    return n_list
