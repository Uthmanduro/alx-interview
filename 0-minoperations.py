#!/usr/bin/python3
"""return the number of minimum operations"""


def minOperations(n):
    """defines the function minperation"""
    arr = []
    for i in range(1, n + 1):
        if n % i == 0:
            arr.append(i)
    return len(arr) + 1
