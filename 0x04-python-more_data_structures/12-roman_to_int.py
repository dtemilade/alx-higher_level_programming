#!/usr/bin/python3
def to_subtract(list_num):
to_sub = 0
max_list = max(list_num)

"""function prototype conditional statement"""
for t in list_num:
if max_list > t:
to_sub = to_sub + t

return (max_list - to_sub)


def roman_to_int(roman_string):
if not roman_string:
return 0

if not isinstance(roman_string, str):
return 0

x = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
y = list(x.keys())

retval = 0
i = 0
j = [0]

for ch in roman_string:
for r_retval in y:
if r_retval == ch:
if x.get(ch) <= i:
retval += to_subtract(j)
j = [x.get(ch)]
else:
j.append(x.get(ch))

i = x.get(ch)

retval += to_subtract(j)

return (retval)
