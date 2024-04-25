#!/usr/bin/python3
def find_peak(list_of_integers):
    """ function that finds a peak in a list of unsorted integers."""
    lt = list_of_integers
    for i in lt[0:]:
        if (i - lt[i-1] == 0 or i - lt[i-1] > 0) and (i - lt[i+1] == 0 or i - lt[i+1] > 0):
            return i
        else:
            return None
