#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if i % 5 == 0 and i % 3 == 0:
            i = "FizzBuzz"
            print("{:s} ".format(i), end="")
        elif i % 5 == 0:
            i = "Buzz"
            print("{:s} ".format(i), end="")
        elif i % 3 == 0:
            i = "Fizz"
            print("{:s} ".format(i), end="")
        else:
            print("{:d} ".format(i), end="")
