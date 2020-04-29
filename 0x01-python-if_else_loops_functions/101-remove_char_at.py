#!/usr/bin/python3
def remove_char_at(str, n):
    new_str = ""
    if n >= 0:
        new_str += str[:n]
        new_str += str[n+1:]
    else:
        new_str = str
    return new_str
