#!/usr/bin/python3
"""class Student that defines a student by: (based on 10-student.py)"""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """instance to Initialize Student attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """method that retrieve dictionary representation of Student instance
        And __dict__function to return an instance of a Class
        """
        if (type(attrs) == list and
                all(type(q) == str for q in attrs)):
            return {w: getattr(self, w) for w in attrs if hasattr(self, w)}
        return self.__dict__

    def reload_from_json(self, json):
        """method that that replaces all attributes of the Student instance"""
        for w, t in json.items():
            setattr(self, w, t)
