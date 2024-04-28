#!/usr/bin/python3
"""Function that returns peak in a list or unsorted integers"""

def merge_func(lefthalf, righthalf):
    """
    Merge sorted sub lists
    
    Args:
        lefthalf (int[]): array of integers
        righthalf (int[]): array of integers
    
    Return: Sorted integer list
    """
    i = j = 0
    result = []

    while (i < len(lefthalf) and j < len(righthalf)):
        if (lefthalf[i] < righthalf[j]):
            result.append(lefthalf[i])
            i += 1
        else:
            result.append(righthalf[j])
            j += 1

    while (i < len(lefthalf)):
        result.append(lefthalf[i])
        i += 1

    while (j < len(righthalf)):
        result.append(righthalf[j])
        j += 1

    return result

def sort_func(int_list):
    """
    Function that sorts arrays using merge sort algorithm

    Args:
        int_list (int) - Integer list

    Return: Sorted integer list
    """
    if len(int_list) <= 1:
        return int_list

    middle = len(int_list) // 2

    lefthalf = sort_func(int_list[:middle])
    righthalf = sort_func(int_list[middle:])
    sorted_list = merge_func(lefthalf, righthalf)

    return sorted_list


def find_peak(list_of_integers):
    """Find peak of an integer list and return it"""
    if (list_of_integers == []):
        return

    sorted_list = sort_func(list_of_integers)
    return sorted_list[-1]
