#!/usr/bin/python3
"""This is 7-base geometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """this class inherits from BaseGeometry"""

    def __init__(self, width, height):
        """instantiates width and height"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

        def area(self):
            """ returns the area of the instance"""
            return self.__width * self.__height

        def __str__(self):
            """Returns string of implementation"""
            return "[Rectangle] {:d}/{:d}"
                       .format(self.__width, self.__height)
