#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if a_dictionary is None or key is None or value is None:
        return
    a_dictionary[key] = value
