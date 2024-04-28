#!/usr/bin/python3
"""Script that finds peak of integer array list"""


def find_peak(list_of_integers):
    """
    Function that finds peak of a array

    Args:
        list_of_integers (int[]): list of integers

    Return: Peak of list
    """
    if len(list_of_integers) < 1:
        return None

    # Binary search
    low = 0
    high = len(list_of_integers) - 1

    while low < high:
        middle = (low + high) // 2

        # check if middle is peak
        if list_of_integers[middle] >= list_of_integers[middle + 1]:
            # if middle is greater or equal to middle + 1 which is on
            # the right side, then peak could be on the lefthalf of
            # the array
            high = middle
        else:
            # if middle is less than right hand neighbhour then peak
            # could be on the right half
            low = middle + 1

    # at the end of the loop, low and high point to the same index
    # which is the peak of the array
    return list_of_integers[low]
