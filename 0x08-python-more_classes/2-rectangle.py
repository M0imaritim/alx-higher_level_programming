#!/usr/bin/python3

"""Defines class, Rectangle"""


class Rectangle:
    """Class defining a rectangle"""

    def __init__(self, width=0, height=0):
        """Method initializing this instance

        Args:
           width: shorter side of rectangle
           height: longer side of rectangle
        """
        self.width = width
        self.height = height

        @property
        def width(self):
            """
            This method returns the value of the width
            """
            return self.__width

        @width.setter
        def width(self, value):
            """ This method alters the value of the width
            Raises:
            TypeError: if width is not an integer
            ValueError: if width is less than zero
            """
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            if value < 0:
                raise ValueError("width must be >= 0")
            self.__width = value

        @property
        def height(self):
            """
            This method returns the value of the height
            """

            return self.__height

        @height.setter
        def height(self, value):
            """ This method defines the height

            Args:
            value: height

            Raises:
            TypeError: if height is not an integer
            ValueError: if height is less than zero

            """
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            if value < 0:
                raise ValueError("height must be >= 0")
            self.__height = value

        def area(self):
            """
            This method calculates the area of Rectangle
            """

            return self.width * self.height

        def perimeter(self):
            """
            This method calculates the perimeter
            """
            if self.width == 0 or self.height == 0:
                return 0
            return (self.width * 2) + (self.height * 2)
