#!/usr/bin/python3
""" function that finds a peak in a list of unsorted integers."""
def find_peak(list_of_integers):
    """function initiation"""
    lt = list_of_integers
    n = len(lt)
    mid = n // 2
    if lt:
        if (mid == 0 or lt[mid] >= lt[mid-1]) and (mid == n-1 or lt[mid] >=lt[mid+1]):
            return lt[mid]
        elif mid > 0 and lt[mid] < lt[mid-1]:
            return find_peak(lt[:mid])
        else:
            return find_peak(lt[mid+1:])
    else:
        return None
