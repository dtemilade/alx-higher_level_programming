#!/usr/bin/python3
for letter in range(97, 123):
    if not(chr(letter)) is 'e' and not(chr(letter)) is 'q':
        print("{}".format(chr(letter)), end="")

