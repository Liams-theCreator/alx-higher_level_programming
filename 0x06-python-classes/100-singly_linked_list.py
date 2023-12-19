#!/usr/bin/python3

class Node:
    def __init__(self, data, next_node=None):
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        return self.__data

    @property
    def next_node(self):
        return self.__next_node

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @next_node.setter
    def next_node(self, value):
        if type(value) is not Node or value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

class SinglyLinkedList:
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        if self.__head is None:
            self.__head = Node(value)
        else:
            current_node = self.__head
            while current_node is not None:
                if self.__head.data >= value:
                    self.__head = Node(value, self.__head)
                    break
                if current_node.next_node is None:
                    current_node.next_node = Node(value)
                    break
                if current_node.next_node.data >= value:
                    current_node.next_node = Node(
                        value, current_node.next_node)
                    break
                current_node = current_node.next_node

    def __str__(self):
        str = ""
        current_node = self.__head
        while current_node is not None:
            new_line = "\n" if current_node.next_node is not None else ""
            str += "%d%s" % (current_node.data, new_line)
            current_node = current_node.next_node
        return str
