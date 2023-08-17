#!/usr/bin/python3
"""function that rotates a 2D matrix 90 degrees clockwise"""


def rotate_2d_matrix(matrix):
    """rotate a 2D matrix and is edited in-place"""
    left, right = 0, len(matrix) - 1

    while left < right:
        top, bottom = left, right
        for i in range(right - left):
            top_left = matrix[top][left + i]
            matrix[top][left + i] = matrix[bottom - i][left]
            matrix[bottom - i][left] = matrix[bottom][right - i]
            matrix[bottom][right - i] = matrix[top + i][right]
            matrix[top + i][right] = top_left
        left += 1
        right -= 1
