#!/usr/bin/python3
"""
module contains function that returns dictionary description with simple data
structure(list, dictionary, string, integer and boolean)
"""


def class_to_json(obj):
    """returns the dictionary description with simple data structure"""
    if hasattr(obj, "__dict__"):
        return vars(obj)
