#!/usr/bin/python3
class Node:
    """Class that defines a node of a singly linked list"""


    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node
    
    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) != int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value
    
    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and type(value) != Node:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value
        
class SinglyLinkedList:
    """Class that defines a singly linked list"""

    def __init__(self):
        self.head = None
    
    def __printlist__(self):
        result = ""
        node = self.head
        while node:
            result += str(node.data) + "\n"
            node = node.next_node
        return result[:-1]

    def sorted_insert(self, value):
        NewNode = Node(value)
        result = ""
        if self.head is None:
            self.head = NewNode
        if(self.head.data > NewNode.data):
            NewNode.next_node = self.head
            self.head = NewNode
        insert_node = self.head
        while insert_node.next_node and insert_node.data>NewNode.data:
            insert_node = insert_node.next_node
        if insert_node.next_node:
            insert_node.next_node = NewNode.next_node
        insert_node.next_node = NewNode