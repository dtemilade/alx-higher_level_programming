#!/usr/bin/python3


def uniq_add(my_list=[]):
uniq_list = set(my_list)
"""variable parameter"""
retval = 0

"""function prototype conditional statement"""
for t in uniq_list:
retval = retval + t

return (retval)
