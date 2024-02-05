#!/usr/bin/python3
"""
Module contains class list
"""


class MyList(list):
    """inherits the attributes of class list

    Args:
        list: class list

    """
    def print_sorted(self):
        """prints sorted list"""
        sorted_lst = self.copy()
        sorted_lst.sort()
        print(sorted_lst)
