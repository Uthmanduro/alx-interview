#!/usr/bin/python3
"""return the number of minimum operations"""


def minOperations(n):
    """returns an integer"""
    if n <= 0 or n == 1:
        return 0
    arr = ["h"]
    exp_result = "h" * n
    cp = arr[0]
    paste = cp
    count = 1
    while len(arr[-1]) <= n:
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
    return 0
