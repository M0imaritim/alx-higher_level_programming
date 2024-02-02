#!/usr/bin/python3
"""
This module contains a function to print my name
"""


def say_my_name(first_name, last_name=""):
    """
    this function prints my full names
    """x
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("my name is {} {}".format(first_name, last_name))
