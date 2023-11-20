#!/usr/bin/python3

def safe_print_division(a, b):
    result = None
    try:
        result = a / float(b)
        return result
    except ZeroDivisionError as err:
        return None
    finally:
        print("Inside result: {}".format(result))
