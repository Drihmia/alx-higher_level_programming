#!/usr/bin/python3
from numpy import dot

def lazy_matrix_mul(m_a, m_b):
    try:
        return dot(m_a, m_b)
    except Exception as e:
        print(e)
