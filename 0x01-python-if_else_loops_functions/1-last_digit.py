#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ld = abs(number % 10)

if number < 0:
    ld *= -1

if ld > 5:
    print("Last digit of %d is %d and is greater than 5" % (number, ld))
elif ld < 6 and ld != 0:
    print("Last digit of %d is %d and is less than 6 and not 0" % (number, ld))
else:
    print("Last digit of %d is %d and is 0" % (number, ld))
