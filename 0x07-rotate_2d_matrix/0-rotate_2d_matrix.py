#!/usr/bin/python3
"""
a module that implements a 2D mathrix Rotation
"""


def rotate_2d_matrix(matrix):
    """
    Rotates a (n x n) 2D matrix 90 degrees clockwise in place
    """
    n = len(matrix)

    # Transpose the matrix
    for x in range(n):  # loop for outer list
        for y in range(x, n):  # loop for inner list
            matrix[x][y], matrix[y][x] = matrix[y][x], matrix[x][y]
            # swap each value of i and J respectively

    # Reverse each row
    for x in range(n):
        matrix[x].reverse()
