#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    num = len(sys.argv)
    if num == 1:
        print("{:d} argument.".format(num - 1))
    elif num == 2:
        print("{:d} argument:".format(num - 1))
    else:
        print("{:d} arguments:".format(num - 1))
    for i in range(num):
        if i == 0:
            continue
        print("{:d}: {:s}".format(i, sys.argv[i]))
