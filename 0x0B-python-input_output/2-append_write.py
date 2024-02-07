#!/usr/bin/python3
"""Module contains a function that appends to a file"""


def append_write(filename="", text=""):
    """Appends a string to a text file and returns number of
       characters added
    """
    with open(filename, 'a+', encoding="utf-8") as f:
        return f.write(text)
