#!/usr/bin/python3
"""defines a function 'canUnlockAll'"""


def canUnlockAll(boxes):
    """returns true if all boxes can be opened else false"""
    length = len(boxes)
    keys = []
    for box in boxes:
        for key in box:
            keys.append(key)
    for index in range(1, len(boxes)):
        if index in keys:
            continue
        else:
            return False
    return True
