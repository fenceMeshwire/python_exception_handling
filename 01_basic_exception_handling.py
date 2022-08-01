#!/usr/bin/env python3

# Python 3.9.5

# 01_basic_exception_handling.py

try:
    f_in = open('error_log.txt')
    for line in f_in:
        print(line , end='')
except BaseException as err:
    print(err)
finally:
    print('End of program')
