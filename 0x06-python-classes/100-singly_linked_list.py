#!/usr/bin/python3
"""module containing a Singly linked list representation"""


class Node:
    """represent a node of a Linked list"""

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if type(value) is not Node:
            if value is not None:
                raise TypeError("next_node must be a Node object")
            else:
                self.__next_node = None
        else:
            self.__next_node = value


class SinglyLinkedList:
    """represent a Singly Linked list"""

    def __init__(self):
        self.__head = None

    def __str__(self):
        """print entire list to stdout"""

        items = ""
        tmp = self.__head
        while tmp is not None:
            items += str(tmp.data)
            tmp = tmp.next_node
            if tmp is not None:
                items += "\n"

        return items

    def sorted_insert(self, value):
        """insert new Node at correct position in list (increasing order)"""

        new_node = Node(value)

        tmp = self.__head
        if (tmp is None) or (tmp.data > new_node.data):
            self.__head = new_node
            new_node.next_node = tmp
        else:
            while (tmp is not None) and (tmp.next_node is not None):
                if tmp.next_node.data > new_node.data:
                    break
                tmp = tmp.next_node

            new_node.next_node = tmp.next_node
            tmp.next_node = new_node
