#!/usr/bin/python3
""" function that finds a peak in a list of unsorted integers."""
def find_peak(list_of_integers):
    lt = list_of_integers
    try:
        for i in lt[0:]:
            if (i - lt[i-1] >= 0) or (i - lt[i+1] >= 0):
                return i
            else:
                return None
    except IndexError:
        return None
