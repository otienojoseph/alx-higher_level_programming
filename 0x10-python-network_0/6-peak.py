#!/usr/bin/python3
"""Function that returns peak in a list or unsorted integers"""

def merge_func(int_list, lb, mid, ub):
    """Merge the sorted sub lists"""
    i = lb, j = mid + 1, k = lb, arr = []
    while (i <= mid && j <= ub):
        if (int_list[i] < int_list[j]):
            arr[k] = int_list[i]
            i++
        else:
            arr[k] = int_list[j]
            j++
        k++

    if (i > mid):
        while (j <= ub):
            arr[k] = int_list[j]
            j++
            k++
    else:
        while (i <= mid):
            arr[k] = int_list[i]
            i++
            k++
    for i in range(len(int_list)):
        int_list[i] = arr[i]

    return int_list

def sort_func(int_list):
    """
    Sorting function that returns a sorted list

    Args:
        int_list (int) - Integer list

    Return: Sorted integer list
    """
    lb = 0
    ub = len(int_list)

    if (lb < ub):
        mid = (lb + ub) // 2
        sort_func(int_list, lb, mid)
        sort_func(int_list, mid + 1, ub)
        merge_func(int_list, lb, mid, ub)

def find_peak(list_of_integers):
    """Find peak of an integer list and return it"""
    if list_of_integers == []:
        return

    sorted_list = sort_func(list_of_integers)

    return sorted_list[-1]
