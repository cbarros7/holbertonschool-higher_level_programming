#!/usr/bin/env python3


def no_c(my_string):
    new = list(my_string)
    new = ''.join(char for char in my_string if char not in 'Cc')
    return new
