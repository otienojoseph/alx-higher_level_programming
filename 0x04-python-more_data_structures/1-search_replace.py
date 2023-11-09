#!/usr/bin/python3

def search_replace(my_list, search, replace):
    ls_copy = my_list[:]

    for i in range(len(ls_copy)):
        if ls_copy[i] == search:
            ls_copy[i] = replace

    return ls_copy
