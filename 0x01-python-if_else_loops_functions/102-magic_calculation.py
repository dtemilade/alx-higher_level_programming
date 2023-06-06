#!/usr/bin/python3
"""Interprete Python bytecode"""
def magic_calculation(a, b, c):
"""Compare a less than b, return c"""
    if a < b:
        return (c)
"""Compare b greater than c, return the below"""
    if c > b:
        return (a + b)
    return (a*b - c)
