#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":
    args = argv[1:]
    arg_len = len(args)

    if arg_len == 0:
        print("0 arguments.")
    elif arg_len == 1:
        print("1 argument.")
    else:
        print("{} arguments:".format(arg_len))

    for i in range(arg_len):
        print("{}: {}".format(i, args[i]))
