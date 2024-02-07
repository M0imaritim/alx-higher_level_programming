#!/usr/bin/python3
"""
module inserts a line of text after each line containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """
    inserts a line of text to a file,
    after each line containing a specific string
    """
    with open(filename, 'r', encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            if line.find(search_string) != -1:
                lines += [new_string]

    with open(filename, 'w', encoding="utf-8") as f:
        f.write("".join(lines))
