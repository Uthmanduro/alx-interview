#!/usr/bin/python3
"""determines if a given data set represents a valid UTF-8 encoding"""


def validUTF8(data):
    """Return: True if data is a valid UTF-8 encoding, else return False"""
    if not isinstance(data, list):   # check if data is a list
        return False
    for item in data:  # check if item is an int
        if not isinstance(item, int):
            return False

        binary = bin(item)[2:]
        if len(binary) > 0 and len(binary) <= 8:  # check if item is 1 byte
            binary = binary.zfill(8)  # fill with 0s to make 8 bits
            if binary.startswith("0"):  # check if item is 1 byte
                continue
            else:
                return False
        elif len(binary) > 8 and len(binary) <= 16:  # check if item is 2 bytes
            sec_byte = binary[8:16]
            if binary.startswith("110") and sec_byte.startswith("10"):
                # check first 3 bits and 2nd byte
                continue
            else:
                return False
        elif len(binary) > 16 and len(binary) <= 24:
            # check if item is 3 bytes
            sec_byte = binary[8:16]
            thd_byte = binary[16:24]
            if binary.startswith("1110") and sec_byte.startswith("10") and\
                    thd_byte.startswith("10"):
                #  check first 4 bits, 2nd byte and 3rd byte
                continue
            else:
                return False
        elif len(binary) > 24 and len(binary) <= 32:
            # check if item is 4 bytes
            sec_byte = binary[8:16]  # extract 2nd byte
            thd_byte = binary[16:24]   # extract 3rd byte
            foth_byte = binary[24:32]  # extract 4th byte
            if binary.startswith("11110") and sec_byte.startswith("10")\
                    and thd_byte.startswith("10")\
                    and foth_byte.startswith("10"):
                continue
            else:
                return False
    return True
