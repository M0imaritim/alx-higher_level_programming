#!/usr/bin/python3
"""
This module consists of a function that adds two integers
"""
def add_integer(a, b=98):
    """ Function that adds two integers or float numbers
    Args:
        a: first value
        b: second value
    Raises:
       TypeError: if a or b is not an integer or float value
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)

    return a + b
