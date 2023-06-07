#!/usr/bin/python3
startval = 0
for alphval in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(alphval - startval)), end="")
    startval = 32 if startval == 0 else 0
