#!/usr/bin/python3


def max_integer(my_list=[]):
    count = len(my_list)
    if count == 0:
        None
    v_max = my_list[0]
    for i in range(count):
        if my_list[i] > v_max:
            v_max = my_list[i]
    return v_max
