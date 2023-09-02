#!/usr/bin/python3
"""Change comes from within"""


def makeChange(coins, total):
    """returns fewest number of coins needed \
        to meet a given amount total"""
    if total <= 0:
        return 0

    init_total = 0
    used_coins = 0
    coins = sorted(coins, reverse=True)
    for coin in coins:
        solution = (total - init_total) // coin
        init_total += solution * coin
        used_coins += solution
        if init_total == total:
            return used_coins
    return -1
