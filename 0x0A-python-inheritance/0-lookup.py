#!/usr/bin/python3
"""
Module contains function that returns the list of attributes and
methods of an object
"""
def lookup(obj):
    """returns the list of attributes and methods of an object"""
    return dir(obj)
