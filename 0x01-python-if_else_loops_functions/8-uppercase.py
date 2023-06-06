#!/usr/bin/python3
def uppercase(str):
    for var_str in str:
        if ord(var_str) >= 97 and ord(var_str) <= 122:
            var_str = chr(ord(var_str) - 32)
            print("{}".format(var_str), end="")
            print("")
