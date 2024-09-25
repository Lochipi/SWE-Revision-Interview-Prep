"""
tips: create a iterator node that would point to the head at first
check if the head is not null - if not null, display the curr node, and assign the iterator to the next node.
Again check if the curr node is null or not, and if not we display the value and we will keep doing this on and on.

if we reach at a point wheer it is null, we stop, there are no iterations to take.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        new_node = Node(value)

        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, value):
        new_node = Node(value)

        if not self.tail:
            self.tail = new_node
        else:
            self.head.next = new_node # assigning the next ele of new node to the current node of the head
            self.head = new_node # and setting the head to the new node

    def iterate(self):
        iterator = self.head

        while self.head:
            print(iterator.value, " ")
            iterator = iterator.next