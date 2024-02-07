#!/usr/bin/python3
"""
Module contains function to return json string to data structure
"""
import json


def from_json_string(my_str):
    """returns object represented by a JSON string"""
    return json.loads(my_str)
