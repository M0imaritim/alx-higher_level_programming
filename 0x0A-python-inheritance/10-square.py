#!/usr/bin/python3
"""This module inherits from 9-rectangle.py"""


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
