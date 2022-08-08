

class Node():
    """Node of Linked List"""

    def __init__(self, value):
        super(Node, self).__init__()
        self.value = value
        self.next = None


class LinkedList():
    """actual Linked List"""

    def __init__(self, value):
        super(LinkedList, self).__init__()
        self.head = Node(value)

    def insert(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            current = self.head
            new_node = Node(value)
            self.head = new_node
            self.head.next = current

    def remove(self):
        if self.head is None:
            return None
        next_node = self.head.next
        head_value = self.head.value
        self.head = next_node
        return head_value

    def reverse_a_linkedlist(self):
        dummy = None  # create new Dummy Node
        while self.head is not None:
            nextNode = self.head.next  # save the next node
            self.head.next = dummy     # point next pointer to newHead
            dummy = self.head          # make dummy equal to old_head
            self.head = nextNode       # move head to the next node
        self.head = dummy
        print('reversed')

    def traverse(self):
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next
        print("----")

    def remove_a_duplicate_nobuffer(self):
        p1 = self.head
        p2 = self.head
        while p1 is not None:
            while p2 is not None:
                if p1.value == p2.value and p1 != p2:
                    print("duplicate here")
                print(p1.value, p2.value)
                p2 = p2.next
            p1 = p1.next


c = LinkedList(2)
c.insert(1)
c.insert(3)
c.insert(4)
c.insert(2)
# c.traverse()
# c.remove()
# c.reverse_a_linkedlist()
c.traverse()
c.remove_a_duplicate_nobuffer()

