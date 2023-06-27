#!/usr/bin/python3
"""Define classes for a singly-linked list."""


class Node:
    """Define __init___ method for node in a singly-linked list."""

    def __init__(self, data, next_node=None):
        """declaring data and next_node for the list"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Assigning data of the Node."""
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Assigning next_node to the method"""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Define __init___ method for singly-linked list."""

    def __init__(self):
        """Initalize a new SinglyLinkedList."""
        self.__head = None

    def sorted_insert(self, value):
        """Insert the node into the list.
        In an ordered numerical position.
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            i = self.__head
            while (i.next_node is not None and i.next_node.data < value):
                i = i.next_node
            new.next_node = i.next_node
            i.next_node = new

    def __str__(self):
        """Introducing print() representation of a SinglyLinkedList."""
        values = []
        i = self.__head
        while i is not None:
            values.append(str(i.data))
            i = i.next_node
        return ('\n'.join(values))
