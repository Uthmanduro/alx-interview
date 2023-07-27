#!/usr/bin/python3
"""determines if a given data set represents a valid UTF-8 encoding"""


def validUTF8(data):
    """Return: True if data is a valid UTF-8 encoding, else return False"""
    try:
        assert type(data) == list
        for num in data:
            assert type(num) == int
    except Exception:
        return False
    for item in data:  # check if item is an int
        binary = item & 0xFF
        binary = bin(binary)[2:].zfill(8)  # convert to binary
        if binary.startswith("0"):  # check if item is 1 byte
            continue
        elif binary.startswith("110") and binary[4:8].startswith("10"):
            continue
        elif binary.startswith("1110") and binary[4:8].startswith("10"):
            continue
        elif binary.startswith("11110") and binary[4:8].startswith("10"):
            continue
        else:
            return False
    return True
