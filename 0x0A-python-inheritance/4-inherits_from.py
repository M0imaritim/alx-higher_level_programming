#!/usr/bin/python3
def inherits_from(obj, a_class):
    """
    returns True or False if object is an instance of a class
    """
    if isinstance(obj, a_class):
        return False
    return type(obj) is a_class
