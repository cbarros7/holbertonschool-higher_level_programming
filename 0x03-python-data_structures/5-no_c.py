#!/usr/bin/python3


def no_c(my_string):
    my_string = ''.join(char for char in my_string if char not in 'Cc')
    return my_string
