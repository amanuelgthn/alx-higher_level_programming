#!/usr/bin/python3
"""
function that finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """
    finds a peak in a list of integers
    """
    if list_of_integers == []:
        return
    for i in range(len(list_of_integers)):
        if i > 0 and i < (len(list_of_integers) - 1):
            if (list_of_integers[i] > list_of_integers[i - 1]
               and list_of_integers[i] > list_of_integers[i+1]):
                return list_of_integers[i]
        elif i == len(list_of_integers) - 1:
            if list_of_integers[i] > list_of_integers[i-1]:
                return list_of_integers[i]
    return list_of_integers[0]
