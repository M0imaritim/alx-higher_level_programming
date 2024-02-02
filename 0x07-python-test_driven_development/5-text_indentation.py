#!/usr/bin/python3
"""
This module contains a function that prints 2 new lines after characters
"""


def text_indentation(text):
    """
    this function prints two new lines after specified punctuatuions
    Args:
        text: text to be splited into new lines
    """


    if not isinstance(text, str):
        raise TypeError("text must be a string")
    n_text = text[:]

    for i in ".?:":
        texty = n_text.split(i)
        n_text = ""
        for j in texty:
            j = j.strip(" ")
            n_text = j + i if n_text is "" else n_text + "\n\n" + j + i
    print(n_text[:-3], end="")
