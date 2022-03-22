#!/usr/bin/python3
"""Algorithm to find the largest in a list"""


def find_peak(list_of_integers):
    """Return the largest from a list unsorted integers."""
    if list_of_integers == []:
        return None

    m = len(list_of_integers)
    if m == 1:
        return list_of_integers[0]
    elif m == 2:
        return max(list_of_integers)

    mid = int(m / 2)
    peak = list_of_integers[mid]
    if peak > list_of_integers[mid - 1] and peak > list_of_integers[mid + 1]:
        return peak
    elif peak < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
    else:
        return find_peak(list_of_integers[mid + 1:])
