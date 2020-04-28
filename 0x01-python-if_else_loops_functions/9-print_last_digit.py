#!/usr/bin/python3
def print_last_digit(number):
    number = number % 10 if number > 0 else abs(number % -10)
    print(number, end="")
    return (number)
