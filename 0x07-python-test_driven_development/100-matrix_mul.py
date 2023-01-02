#!/usr/bin/python3
"""Multiplies 2 matrices"""


def matrix_mul(m_a, m_b):
    """ Multiplies 2 matrices"""
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b,list):
        raise TypeError("m_b must be a list")
    if not all(isinstance(item, list) for item in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(item, list) for item in m_b):
        raise TypeError("m_b must be a list of lists")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    if not all(isinstance(item, (int, float)) for l in m_a for item in l):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(item, (int, float)) for l in m_b for item in l):
        raise TypeError("m_b should contain only integers or floats")

    result = [list(str(0) * 3) for i in range(len(m_a))]
    
    for row in m_a:
        if len(row) != len(m_a[0]):
            raise TypeError("each row of m_a must be of the same size")
        if len(row) != len(m_b[0]):
            raise TypeError("each row of m_b must be of the same size")
        for i in range(len(m_a)):
            for j in range(len(m_b[0])):
                for k in range(len(m_b)):
                    try:
                        result[i][j] += m_a[i][k] * m_b[k][j]
                    except:
                        raise ValueError("m_a and m_b can't be multiplied")
    return result
