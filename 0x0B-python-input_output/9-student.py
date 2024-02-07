#!/usr/bin/python3
"""Module contains class Student"""


class Student:
    """class instantiating student"""

    def __init__(self, first_name, last_name, age):
        """function initializing first_name, last_name and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation of a Student"""
        return vars(self)
