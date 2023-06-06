#!/usr/bin/python3
for dec_num in range(0, 100):
    if dec_num == 99:
        print("{}".format(dec_num))
    else:
        print("{:02}".format(dec_num), end=", ")
