#!/usr/bin/python3
"""determines if a given data set represents a valid UTF-8 encoding"""


def validUTF8(data):
    """Return: True if data is a valid UTF-8 encoding, else return False"""
    if not isinstance(data, list):
        return False
    for item in data:
        if not isinstance(item, int):
            return False

        binary = bin(item)[2:]
        if len(binary) > 0 and len(binary) <= 8:
            binary = binary.zfill(8)
            if binary.startswith("0"):
                continue
            else:
                return False
        elif len(binary) > 8 and len(binary) <= 16:
            binary = binary.zfill(16)
            sec_byte = binary[8:16]
            if binary.startswith("110") and sec_byte.startswith("10"):
                continue
            else:
                return False
        elif len(binary) > 16 and len(binary) <= 24:
            binary = binary.zfill(24)
            sec_byte = binary[8:16]
            thd_byte = binary[16:24]
            if binary.startswith("1110") and sec_byte.startswith("10") and\
                    thd_byte.startswith("10"):
                continue
            else:
                return False
        elif len(binary) > 24 and len(binary) <= 32:
            binary = binary.zfill(32)
            sec_byte = binary[8:16]
            thd_byte = binary[16:24]
            foth_byte = binary[24:32]
            if binary.startswith("11110") and sec_byte.startswith("10")\
                    and thd_byte.startswith("10")\
                    and foth_byte.startswith("10"):
                continue
            else:
                return False
        else:
            return False
    return True
