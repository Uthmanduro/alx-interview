#!/usr/bin/python3
"""return the number of minimum operations"""


def minOperations(n):
    """returns an integer"""
    if n <= 0:
        return 0
    if n == 1:
        return 1
    arr = ["h"]
    exp_result = "h" * n
    cp = arr[0]
    paste = cp
    count = 1
    while True:
        paste += cp
        arr.append(paste)
        count += 1
        if arr[-1] == exp_result:
            return count
        if len(exp_result) % len(arr[-1]) == 0:
            cp = arr[-1]
            count += 1
            paste += cp
            arr.append(paste)
            count += 1
            if arr[-1] == exp_result:
                return count
