#!/usr/bin/python3
"""module contains inherits_from function"""


def inherits_from(obj, a_class):
    """
    returns True or False if object is an instance of a class
    """
    if type(obj) is a_class:
        return False
    return isinstance(obj, a_class)
