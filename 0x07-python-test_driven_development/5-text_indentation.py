#!/usr/bin/python3
"""Prototype for text-indentation function."""


def text_indentation(text):
    """Declaration and the required process as follows:"""
    if not isinstance(text, str):
        raise TypeError("text is always a string")
    tstval = 0
    while tstval < len(text) and text[tstval] == ' ':
        tstval += 1
    while tstval < len(text):
        print(text[tstval], end="")
        if text[tstval] == "\n" or text[tstval] in ".?:":
            if text[tstval] in ".?:":
                print("\n")
            tstval += 1
            while tstval < len(text) and text[tstval] == ' ':
                tstval += 1
            continue
        tstval += 1
