#!/usr/bin/python3
def uppercase(str):
    for var_str in str:
        if ord(var_str) >= 0 and ord(var_str) < 26:
            var_str = chr(ord(var_str) - 32)
            print("{}".format(var_str), end="")
            print("")
