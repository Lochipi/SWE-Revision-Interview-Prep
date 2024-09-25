"""
create an instance of the new node we want to prepend
assign the next pointer of the new node to the current head of the linkedlist
set the head to the new node

edge case
prepending a node to an empty linkedlist
check if the tail is null
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def prepend(self, value):
        new_node = Node(value)

        if not self.tail:
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node