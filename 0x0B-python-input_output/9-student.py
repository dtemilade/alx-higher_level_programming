#!/usr/bin/python3
"""class Student that defines a student"""


class Student:
    """The class; template to perform the task."""

    def __init__(self, first_name, last_name, age):
        """instance to Initialize Student attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """__dict__function to return an instance of a Class"""
        return self.__dict__
