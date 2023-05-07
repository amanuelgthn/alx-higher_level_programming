#!/usr/bin/python3
"""M
Module containing the matrix_mul function
"""


def matrix_mul(m_a, m_b):
    """
    Function that multiplies two matrices
    """
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    if any(not isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if any(not isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if m_a == [] or m_a == [[]]:
        raise TypeError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise TypeError("m_b can't be empty")
    for row in m_a:
        for element in row:
            if not isinstance(element, (float, int)):
                raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        for element in row:
            if not isinstance(element, (float, int)):
                raise TypeError("m_b should contain only integers or floats")
    if not all(len(m_a[i-1]) == len(m_a[i]) for i in range(1, len(m_a))):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(m_b[i-1]) == len(m_b[i]) for i in range(1, len(m_b))):
        raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    m = len(m_a)
    p = len(m_b[0])
    n = len(m_b)
    product = []
    for i in range(0, m):
        c = []
        for j in range(0, p):
            c_sum = 0
            for k in range(0, n):
                c_sum+= m_a[i][k] * m_b[k][j]
            c.append(c_sum)
        product.append(c)
    return product
            


