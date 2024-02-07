#!/usr/bin/python3
"""
module defines pascal's triangle in form of a matrix
"""


def pascal_triangle(n):
    """returns a list of integers representing  the Pascal's triangle"""

    """create an empty list"""
    triangle = []

    """iterate through elements of the list"""
    for i in range(n):
        row = []
        """iterate through elements of inside lists"""
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)

            else:
                prev_row = triangle[i - 1]
                left_value = prev_row[j - 1]
                right_value = prev_row[j]
                row.append(left_value + right_value)
        triangle.append(row)
    return triangle
