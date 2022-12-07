#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newlist = []
    for i in matrix:
        newlist.append(list(map(lambda x: x**2, i)))
    return newlist
