## we know what circular linked list is, now we implement in python.


class Node(value):
    self.value = value
    self.prev = None
    self.nxt = None

class CircularLinkedList:
    """CircularLinkedList.

    init - to create a fixed size CircularLinkedList

    Insert
    Delete

    """
    self.head = None

    def __init__(self, value):
        self.insert(value)

    def insert(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            new_node = Node(value)

            # linking new nonde to head
            self.head.prev = new_node
            new_node.nxt = self.head

            if self.head.prev is not None:
                # prev node exists
                last_node = self.head.prev
                last_node.nxt = new_node
                new_node.prev = last_node

    def traverse(self):
        current = self.head
        while current.nxt:
            print(str(current.value), ' ')
            current = current.nxt


if __name__ == "__main__":
    c = CircularLinkedList(4)
    c.insert(9)
    c.insert(7)
    c.insert(1)
    c.insert(0)
    c.traverse()






