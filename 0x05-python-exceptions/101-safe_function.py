#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    result = None
    try:
        result = fct(*args)
        return result
    except Exception as error:
        sys.stderr.write("Exception: {}\n".format(error))
    return result
