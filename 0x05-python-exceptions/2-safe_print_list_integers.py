#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    if my_list is None:
        my_list = []
    printed = 0
    for i in my_list[:x]:
        try:
            print("{:d}".format(i), end='')
        except (TypeError, ValueError, IndexError):
            continue
        else:
            printed += 1
    print()
    return printed
