#!/usr/bin/python3


def element_at(my_list, idx):
    if idx < 0:
        None
    elif idx > len(my_list):
        None
    for i in range(len(my_list)):
        if i == idx:
            return i
        else:
            continue
