#!/usr/bin/python3
'''A class square that defines a square'''


class Square:
    '''Instantiating a private attribute size'''
    def __init__(self, size=0):
        self.__size = size

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

    def area(self):
        '''returns the area of the square'''
        return self.__size ** 2

    def my_print(self):
        '''returns the area in form of #'''
        if not self.__size:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
