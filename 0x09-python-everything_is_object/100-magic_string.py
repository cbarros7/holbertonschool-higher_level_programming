#!/usr/bin/python3
def magic_string():
    setattr(magic_string, 'str', getattr(magic_string, 'str', -1) + 1)
    return ('Holberton' + ', Holberton' * magic_string.str)
