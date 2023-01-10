#!/usr/bin/python3
"""Pascal Triangle"""


def pascal_triangle(n):
    """returns a list of lists of integers representing
       the Pascal triangle
    """
    row = old = res = []
    if n <= 0:
        return res
    for i in range(n):
        row = [1]
        if i != 0:
            for j in range(len(old)):
                try:
                    next_i = old[j + 1]
                except IndexError:
                    next_i = 0
                val = old[j] + next_i
                row.append(val)
        old = row
        res.append(row)
    return res
