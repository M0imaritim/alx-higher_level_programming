#!/usr/bin/python3
"""Module that contains class student"""


class Student:
    """class instantiating student"""

    def __init__(self, first_name, last_name, age):
        """function initializing first_name, last_name and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student"""

        """check if attrs is a list and all its elements are strings"""
        if isinstance(attrs, list) and all(isinstance(attr, str)
                                           for attr in attrs):

            """
            if condition is met use this dict comprehension for representation
            """
            return {attr: getattr(self, attr) for attr in attrs
                    if hasattr(self, attr)}
        else:
            return vars(self)
