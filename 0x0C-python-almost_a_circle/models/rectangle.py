#!/usr/bin/python3
"""module contains class Rectangle that inherits from class Base"""


from models.base import Base


class Rectangle(Base):
    """Class initializing rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """constructor with instance attributes"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """
        This method returns the value of the width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """ This method alters the value of the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        This method returns the value of the height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """ This method defines the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Method to return value of x"""
        return self.__x

    @x.setter
    def x(self, value):
        """This method defines x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Method returns the value of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Method defines y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns the area value of Rectangle"""
        return self.__width * self.__height

    def display(self):
        """ prints in stdout the Rectangle instance with the character #"""
        for _ in range(self.__y):
            """introduced cartesian plain to print rectangle at"""
            print()
        for i in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """
        returns string representation of attributes.
        It is overidden in this case.
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".\
            format(self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        if args is not None and len(args) != 0:
            attrs = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                setattr(self, attrs[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """returns the dictionary representation of Rectangle"""
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
