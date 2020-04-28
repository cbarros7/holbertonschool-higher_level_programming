#!/usr/bin/python3
def uppercase(str):
    new_text = ""
    for i in (str):
        char = ord(i)
        if char >= ord('a') and char <= ord('z'):
            char = char - 32
            new_text = chr(char)
        else:
            new_text = i
        print("{:s}".format(new_text), end="")
    print("")
