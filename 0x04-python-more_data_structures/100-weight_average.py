#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    else:
        mult = 0
        suma = 0
        for x in my_list:
            mult += x[0] * x[1]
        for x in my_list:
            suma += x[1]
        return mult/suma
