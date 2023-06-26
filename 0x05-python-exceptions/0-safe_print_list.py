#!/usr/bin/python3
"""Prototype  function that prints x elements of a list
Returns the real number of elements printed
"""



def safe_print_list(my_list=[], x=0):
"""introduce variable parameter"""
retval = 0
"""introduce conditional statement"""
for tstval in range(x):
try:
print("{}".format(my_list[tstval]), end="")
retval += 1
except IndexError:
break
print("")
return (retval)
