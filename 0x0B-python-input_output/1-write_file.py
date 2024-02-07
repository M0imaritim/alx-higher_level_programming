#!/usr/bin/python3
"""Module contains function to write into a file"""


def write_file(filename="", text=""):
    """writes a string to a text file & returns the # of characters written"""
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
