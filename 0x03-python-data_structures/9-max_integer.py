#!/usr/bin/python3

def max_integer(my_list=[]):
    list_len = len(my_list)

    if list_len != 0:
        my_list.sort()
        return my_list[-1]
    else:
        return None
