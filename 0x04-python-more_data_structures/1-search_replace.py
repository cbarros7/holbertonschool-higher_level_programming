#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = my_list.copy()
    for n, i in enumerate(new):
        if i == search:
            new[n] = replace
    return new
