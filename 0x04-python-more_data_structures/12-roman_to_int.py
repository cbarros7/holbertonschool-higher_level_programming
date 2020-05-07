#!/usr/bin/python3
def roman_to_int(roman_string):
    n_rom = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000}
    value = 0
    num = 0
    len_n = roman_string
    if type(roman_string) is not str:
        return 0
    if roman_string is None:
        return 0
    for num in range(num, len(len_n)):
        if num < len(len_n) - 1 and n_rom[len_n[num]] < n_rom[len_n[num + 1]]:
            value -= n_rom[len_n[num]]
        else:
            value += n_rom[len_n[num]]
    return value
