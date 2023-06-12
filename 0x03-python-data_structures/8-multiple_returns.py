#!/usr/bin/python3
"""function that returns a tuple with string length & its first character."""
def multiple_returns(sentence):
    if sentence == "":
        return (0, None)
    return (len(sentence), sentence[0])
