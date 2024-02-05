#!/usr/bin/python3
"""module contains a class"""


class BaseGeometry:
    """This is a class with two methods"""
    def area(self):
        """function with no implementation"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """function that validates value"""
        if value not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if self.value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
