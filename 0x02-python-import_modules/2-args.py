#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    num = len(sys.argv)
    if num == 1:
        print("{:d} arguments.".format(num - 1))
    elif num == 2:
        print("{:d} argument:".format(num - 1))
    else:
        print("{:d} arguments:".format(num - 1))
    for i in range(1, num):
        print("{:d}: {:s}".format(i, sys.argv[i]))
