#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    if my_list is None:
        my_list = []
    printed = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end='')
        except (TypeError, ValueError, IndexError):
            continue
        else:
            printed += 1
    print()
    return printed
