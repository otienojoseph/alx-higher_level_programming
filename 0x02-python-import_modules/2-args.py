#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":
    args = argv[1:]
    arg_len = len(args)

    if arg_len == 0:
        print("{} arguments.".format(arg_len))
    elif arg_len == 1:
        print("{} argument:".format(arg_len))
    else:
        print("{} arguments:".format(arg_len))

    for i, arg in enumerate(args, 1):
        print("{}: {}".format(i, arg))
