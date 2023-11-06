#!/usr/bin/python3

def no_c(my_string):
    list_string = list(my_string)

    for i in range(len(list_string)):
        if list_string[i] == 'c' or list_string[i] == 'C':
            list_string[i] = ''
        else:
            continue

    return ''.join(list_string)
