


class Node():
	"""docstring for Node"""
	def __init__(self, value):
		super(Node, self).__init__()
		self.value = value
		self.next = None
		

class LinkedList():
	"""docstring for LinkedList"""

	def __init__(self, arg):
		super(LinkedList, self).__init__()
		self.head = None

	def insert(self, value):
		if self.head == None:
			self.head = Node(value)
		else:
			current = self.head
			new_node = Node(value)
			self.head = new_node
			self.head.next = current


	def reverse_a_linkedlist(self):
		dummy = None # create new Dummy Node
		while self.head != None:
			nextNode = self.head.next # save the next node
			self.head.next = dummy # point next pointer to newHead
			dummy = self.head # make dummy equal to old_head
			self.head = nextNode # move head to the next node
		self.head = dummy
		print('reversed')

	def traverse(self):
		current = self.head
		while current != None:
			print(current.value)
			current = current.next
		print("----")


c = LinkedList(2)
c.insert(3)
c.insert(4)
c.insert(5)
c.insert(6)
c.traverse()
c.reverse_a_linkedlist()
c.traverse()

		



