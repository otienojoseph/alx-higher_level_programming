#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    copied_list = my_list[:]
    list_len = len(my_list)

    for i in range(list_len):
        if idx < 0 or idx >= list_len:
            return copied_list
        else:
            copied_list[idx] = element
            return copied_list
