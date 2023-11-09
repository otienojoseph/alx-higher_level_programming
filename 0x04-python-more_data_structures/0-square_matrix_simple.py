#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    #   list comprehession
    #   result = [[x ** 2 for x in row] for row in matrix]
    def double_list(ls=[]):
        res = []

        for i in range(len(ls)):
            res.append(ls[i] ** 2)

        return res

    result = list(map(double_list, matrix))
    return result
