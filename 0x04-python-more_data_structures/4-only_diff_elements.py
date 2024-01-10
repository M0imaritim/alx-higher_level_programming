#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    if set_1 is None or set_2 is None:
        return
    set_3 = set_1.difference(set_2)
    set_4 = set_2 - set_1
    return set_3 | set_4
