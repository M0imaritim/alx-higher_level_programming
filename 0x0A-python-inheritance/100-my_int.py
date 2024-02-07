#!/usr/bin/python3
"""Module contains class Myint"""


class MyInt(int):
    """Class inherits from super class int"""

    def __eq__(self, other):
        """Method inverted to != operator"""
        return int.__ne__(self, other)

    def __ne__(self, other):
        """ Method inverted to == operator """
        return int.__eq__(self, other)
