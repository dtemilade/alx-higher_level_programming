#!/usr/bin/python3
for low_alph in range(97, 123):
    if chr(low_alph) is not 'e' and chr(low_alph) is not 'q':
        print("{}".format(chr(low_alph)), end="")
