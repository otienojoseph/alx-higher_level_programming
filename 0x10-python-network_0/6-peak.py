#!/usr/bin/python3
"""Function that returns peak in a list or unsorted integers"""


def sort_func(int_list):
    """
    Sorting function that returns a sorted list

    Args:
        int_list (int) - Integer list

    Return: Sorted integer list
    """
    list_len = len(int_list)

    for i in range(list_len):
        swapped = False

        for j in range(0, list_len - i - 1):
            if int_list[j] > int_list[j + 1]:
                int_list[j], int_list[j + 1] = int_list[j + 1], int_list[j]
                swapped = True
        if swapped == False:
            break

    return int_list


def find_peak(list_of_integers):
    if list_of_integers == []:
        return

    sorted_list = sort_func(list_of_integers)

    return sorted_list[-1]
