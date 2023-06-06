#!/usr/bin/python3
def fizzbuzz():
    for retval in range(1, 101):
        if retval % 3 == 0 and retval % 5 == 0:
            print("FizzBuzz ", end="")
        elif retval % 3 == 0:
            print("Fizz ", end="")
        elif retval % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(retval), end="")
