#!/usr/bin/python3
"""
module contains function checking if object is instance of class
"""


def is_kind_of_class(obj, a_class):
    """returns True or False if obj is an instance of a class or inherited
    """
    return isinstance(obj, a_class)
