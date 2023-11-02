#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":
    args = argv[1:]
    arg_len = len(args)
    sum = 0

    for i in range(arg_len):
        sum += int(args[i])

    print("{:d}".format(sum))
