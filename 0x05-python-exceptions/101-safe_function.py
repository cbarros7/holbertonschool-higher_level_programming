#!/usr/bin/python3
from sys import stderr


def safe_function(fct, *args):
    result = 0
    try:
        result = fct(args[0], args[1])
        return result
    except ZeroDivisionError as e:
        print("Exception: {}".format(e), file=stderr)
        return None
    except IndexError as e:
        print("Exception: {}".format(e), file=stderr)
        return None
