#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    # check length of tuple, if less than 2
    if len(tuple_a) < 2:
        # append 0 to the tuple
        tuple_a += (0,) * (2 - len(tuple_a))
    elif len(tuple_b) < 2:
        tuple_b += (0,) * (2 - len(tuple_b))

    res = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return res
