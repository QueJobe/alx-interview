#!/usr/bin/python3
"""
Module to rotate a 2D matrix by 90 degrees clockwise
"""


def rotate_2d_matrix(matrix):
    """
    Rotate a nxn 2D matrix by 90 degrees clockwise

    Args:
        matrix: The n x n matrix to rotate

    Return:
        Nothing: The matrix modified in-place
    """

    n = len(matrix)

    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for row in matrix:
        row.reverse()
