#!/usr/bin/python3
"""log parsing exercise"""
import sys


count = 0
codes = {'200': 0, '301': 0, '400': 0, '401': 0,
         '403': 0, '404': 0, '405': 0, '500': 0}
file_size = 0
try:
    for line in sys.stdin:
        count += 1
        args = line.split()
        try:
            file_size += int(args[-1])
            if args[-2] in codes:
                codes[args[-2]] += 1
        except (ValueError, IndexError):
            pass
        if count % 10 == 0:
            print("File size: {}".format(file_size))
            for key, value in codes.items():
                if value == 0 or not str(value).isdigit():
                    continue
                print("{}: {}".format(key, value))
    print("File size: {}".format(file_size))
    for key, value in codes.items():
        if value == 0 or not str(value).isdigit():
            continue
        print("{}: {}".format(key, value))
except KeyboardInterrupt:
    print("File size: {}".format(file_size))
    for key, value in codes.items():
        if value == 0 or not str(value).isdigit():
            continue
        print("{}: {}".format(key, value))
