#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if isinstance(value, int):
            print(int("{:d}".format(value)))
            return True
    except:
        return False
