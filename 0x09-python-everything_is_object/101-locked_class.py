#!/usr/bin/python3
"""Prototype function locked class."""


class LockedClass:
    """a class LockedClass with no class or object attribute,prevents the user
    from dynamically creating other new instance attributes, except first_name
    """

    __slots__ = ["first_name"]
