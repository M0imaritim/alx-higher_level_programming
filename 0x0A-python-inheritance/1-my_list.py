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
        sorted_lst = sorted(self, key=lambda x: (isinstance(x, int), x))
        print(sorted_lst)
