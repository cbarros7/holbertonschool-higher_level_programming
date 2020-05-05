#!/usr/bin/python3


def max_integer(my_list=[]):
    count = len(my_list)
    if count == 0:
        None
    for i in range(count):
        for j in range(i):
            if my_list[i] < my_list[j]:
                continue
            else:
                return my_list[i]
