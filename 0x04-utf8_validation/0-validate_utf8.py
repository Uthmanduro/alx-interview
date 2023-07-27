#!/usr/bin/python3
"""determines if a given data set represents a valid UTF-8 encoding"""


def validUTF8(data):
    """Return: True if data is a valid UTF-8 encoding, else return False"""
    if not isinstance(data, list):
        return False
    for item in data:
        if not all([isinstance(item, int)]):
            return False
    for item in data:
        binary = bin(item)[2:]
        second_byte = binary[8:16]
        third_byte = binary[16:24]
        fourth_byte = binary[24:32]
        if len(binary) <= 8 or binary[:1] == "0":
            continue
        elif len(binary) > 8 and len(binary) <= 16 and binary[:3] == "110"\
                and second_byte[:2] == "10":
            continue
        elif len(binary) > 16 and len(binary) <= 24 and binary[:4] == "1110"\
                and second_byte[:2] == "10" and third_byte[:2] == "10":
            continue
        elif len(binary) > 24 and len(binary) <= 32 and binary[:5] == "11110"\
                and second_byte[:2] == "10" and third_byte[:2] == "10"\
                and fourth_byte[:2] == "10":
            continue
        else:
            return False
    return True
