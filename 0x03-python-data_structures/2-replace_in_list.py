#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    list_len = len(my_list)

    for i in range(list_len):
        if idx < 0 or idx >= list_len:
            return my_list
        else:
            my_list[idx] = element
            return my_list
