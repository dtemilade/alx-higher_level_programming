#!/usr/bin/python3


def weight_average(my_list=[]):
"""function prototype conditional statement"""
if not my_list:
return 0

j = 0
i = 0

for k in my_list:
j += k[0] * k[1]
i += k[1]

return (j / i)
