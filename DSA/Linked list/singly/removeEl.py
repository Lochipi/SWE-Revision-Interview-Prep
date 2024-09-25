"""
You can remove, beginning, end, or anywhere of the linked list, or also the only element in the ll that you want to remove.

a) removing in the beginning:
head              tail
1   ->  2->  3 ->  4 -> None      rem - 1
       head
     move head to the next value -> points to 2

       edge case
in the case where we find we have one element, and we have to point our head to the next node, which would be null - 
   and remember our tail and head were pointing to the only element right? so the tail woud still point to the only element although we have pointed the head to the next
Solution -if you've already pointed the head to null, let the tail point to null as well.

b) remove the middle element
head        tail
1   ->  2->  3 -> None       rem - 2

1 -> 3, move the next pointer of 1 to 3.

c) remove the last element
head              tail
1   ->  2->  3 ->  4 -> None      rem - 4

iterate to the end of the tail where its next is None
let the tail points to the node that was before 4
let the next now of this prev element point to null

d) remove the only element
head/tail
  1 -> None     remove 1

  delete the element


Note:

If you want to perform any operations of removing, an edge case you should check out is find out if it is null/none, and return from the function and do nothing. 
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList: 
    def __init__(self):
        self.head = None
        self.tail = None

    def removeEl(self, value):
        if not self.head:  # case 1
            return
        
        #remove the first node
        if self.head.value == value: # case 2
            self.head = self.head.next
            if self.head is None: # if not self.head  # third case, 3
                self.tail = None
            return
        iterator = self.head
        while iterator.next:
            if iterator.next.value == value:
                iterator.next = iterator.next.next
                if not iterator.next:
                    self.tail = iterator
                return
            iterator = iterator.next


"""
in the case where we've iterated and find that our number that we need to remove is the last element, and if we point our pointer to ``iterator.next.next`` it will point to null right?
   - so the tail would still point to the last node(element we removed), in this case we can make our tail point to the prev elemtnt that became the last element now after removal
   eg:
   i = iterator
   head(1)              tail(4)
   1   ->  2->  3 ->  4 -> None      rem - 4
                i

    if this is all the case, 
     we can check if the last node is null( 3 -> None) we do update on the tail to point to prev element
                3 -> None
                tail -> 3
    again if we can't find the node we need to delete, just keep iterating.
"""

"""
Time and space complexity
a) inserting at the beginning(prepend) - O(1). We're only shifting the pointers. The number of steps here is constant and not affected by the size of the items on the linked list.
    - at the end would still be constant
b) deleting an item.
   - at the beginning -You just adjust the head pointer to the next node.
   - Deletion at the end or at an arbitrary position: This takes O(n) time, where n is the number of nodes in the list. 
     Since you only have a reference to the head and not to the previous node, you need to traverse the list to find the node before the one you want to delete.
c) Traversal:
    O(n) (you need to visit each node one by one). where n is the number of nodes(elements).
d) Searching:
    O(n) (you must traverse the list to find an element).
"""

"""
when to use?

- when you need constant time insertions or deletions
- when you dont know how many items will be in the list
- when you want to insert an element at the middle of the linked list
"""