# let the pointer that points to the next node in the last node points to the new node
# 1 -> 2 -> 3 -> 4 -> 5 -> Null
                    # 5 -> 6 
                    # 6 -> Null
# update the tail to point to the new node, 6

"""
an edge case when appending a linkedlist when the list is empty
- let the head and tail point to this new node

check if the ll is empty -> check the head if it is pointing to none
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

        if self.head is None and self.tail is None: # if not self.head
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
            new_node.next = self.head
            self.head = new_node
    
    def iterate(self):
        iterator = self.head

        while iterator:
            print(iterator.value + " ")
            iterator = iterator.next

    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

# an instance of the linkedlist
ll = LinkedList()

# appending some values
ll.append(2)
ll.append(8)
ll.append(12)

# printing the list
ll.print_list() # Output: 2 -> 4 -> 8 -> None