#!/usr/bin/python3
"""class Student that defines a student by: (based on 9-student.py)"""


class Student:
    """The class; template to perform the task."""

    def __init__(self, first_name, last_name, age):
        """instance to Initialize Student attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """method that retrieves a dictionary representation of a Student instance
        And __dict__function to return an instance of a Class
        """
        if (type(attrs) == list and
                all(type(q) == str for q in attrs)):
            return {w: getattr(self, w) for w in attrs if hasattr(self, w)}
        return self.__dict__
