#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for key in list(a_dictionary.keys()):
        if a_dictionary[key] == value:
            a_dictionary.pop(key)
    return a_dictionary
