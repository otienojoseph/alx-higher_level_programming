#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":
    arg_len = len(argv)

    if arg_len < 2:
        print("0 arguments.")
    elif arg_len == 2:
        print("1 argument.")
    else:
        print("{} arguments:".format(arg_len - 1))

    for i in range(1, arg_len):
        print("{}: {}".format(i, argv[i]))
