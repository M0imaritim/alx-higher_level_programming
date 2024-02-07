#!/usr/bin/python3
"""This module inherits from 9-rectangle.py"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class square inherits from superclass Rectangle"""

    def __init__(self, size):
        """Instantiation with size"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """returns the aquare of size"""
        return super().area()

    def __str__(self):
        """returns  printable string """
        return "[Square] {}/{}".format(self.__size, self.__size)
