#!/usr/bin/python3
"""module contains a function to create an object from JSON file"""
import json


def load_from_json_file(filename):
    """
    function that creates an object from a JSON file
    """
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
