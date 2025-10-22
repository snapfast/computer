"""
this is doubly-circular linked list is, now we implement in python.
"""


class Node():
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.nxt = None


class CircularLinkedList:
    """CircularLinkedList.

    init - to create a fixed size CircularLinkedList

    Insert
    Delete

    """

    def __init__(self):
        self.head = None

    def insert(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            new_node = Node(value)

            """ if there is exists a previous node to head,
            we take that last_node, add new_node to next of last.
            and add last_node to the previous of new_node.
            """
            if self.head.prev is not None:
                # prev node exists
                last_node = self.head.prev
                last_node.nxt = new_node
                new_node.prev = last_node

            """ if there is no next node to head,
            we add new_node as next node to head.
            """
            if self.head.nxt is None:
                self.head.nxt = new_node
                new_node.prev = self.head

            # linking new node to head, will be done in all cases.
            self.head.prev = new_node
            new_node.nxt = self.head
        
    def delete(self, value):
        current = self.head
        while (current.value != value and current == self.head):
            current = current.nxt
        current.prev.nxt = current.nxt
        current.nxt.prev = current.prev

    def traverse(self):
        current = self.head
        print(current.value, end="->")
        while current.nxt != self.head:
            print(str(current.nxt.value), end="->")
            current = current.nxt
        print("\n")


if __name__ == "__main__":
    c = CircularLinkedList()
    c.insert(9)
    c.insert(7)
    c.insert(1)
    c.insert(0)
    c.traverse()
    c.delete(7)
    c.delete(1)
    c.delete(4)
    c.traverse()
