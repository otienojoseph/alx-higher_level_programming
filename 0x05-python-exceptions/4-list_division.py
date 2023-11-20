#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = []

    try:
        for idx in range(list_length):
            result.push(my_list_1[idx] / float(my_list_2[idx]))
    except ZeroDivisionError:
        result.push(0)
        print("{}".format("division by 0"))
    except TypeError:
        result.push(0)
        print("{}".format("wrong type"))
    except IndexError:
        print("{}".format("out of range"))
    finally:
        
