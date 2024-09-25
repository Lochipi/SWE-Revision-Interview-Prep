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
        new_node.next = self.head
        self.head = new_node
        if not self.tail:
            self.tail = new_node

    def remove(self, value):
        if not self.head:
            return
        if self.head.value == value:
            self.head = self.head.next
            if not self.head:
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

    def iterate(self):
        iterator = self.head
        while iterator:
            print(iterator.value + " ")
            iterator = iterator.next


class ShoppingCart:
    def __init__(self):
        self.items = LinkedList()

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def display_cart(self):
        print("Items in the shopping cart: ")
        self.items.iterate()


cart = ShoppingCart()
cart.add_item("Apple")
cart.add_item("Banana")
cart.add_item("Orange")

cart.display_cart()

cart.remove_item("Orange")
cart.display_cart()