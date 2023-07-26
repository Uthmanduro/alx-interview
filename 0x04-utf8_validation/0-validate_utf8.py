#!/usr/bin/env
"""determines if a given data set represents a valid UTF-8 encoding"""


def validUTF8(data):
    """Return: True if data is a valid UTF-8 encoding, else return False"""
    for item in data:
        return len(bytes(item)) < 128
