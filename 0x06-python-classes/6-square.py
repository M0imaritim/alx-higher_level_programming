#!/usr/bin/python3
'''A class square that defines a square'''


class Square:
    '''Instantiating a private attribute size'''
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        '''new assignment of values to an attribute'''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        '''modifying values to attribute position'''
        if not isinstance(value, tuple) or len(value) != 2 or not\
           isinstance(value[0], int) or not isinstance(value[1], int) or\
           value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple\
            of 2 positive integers")

        self.__position = value

    def area(self):
        '''returns the area of the square'''
        return self.__size ** 2

    def my_print(self):
        '''returns the area in form of #'''
        if self.__size == 0:
            print()
        else:
            for i in range(self.position[1]):
                print()
            for i in range(0, self.__size):
                for j in range(self.__position[0]):
                    print(" ", end='')
                for _ in range(self.size):
                    print("#", end="")
                print()
