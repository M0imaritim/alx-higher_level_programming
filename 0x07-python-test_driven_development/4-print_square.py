#!/usr/bin/python3
"""
This module contains a function that prints a squatre with the character #
"""


def print_square(size):
    """
    this function prints a square in form of # characters
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")

    for j in range(size):
        print('#' * size)
