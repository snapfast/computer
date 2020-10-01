


class Node(value):
	"""docstring for Node"""
	def __init__(self, value):
		super(Node, self).__init__()
		self.left = None
		self.value = value
		self.right = None

class BST(object):
	"""docstring for BST"""
	def __init__(self, root):
		super(BST, self).__init__()
		self.root = root
		
	def insert_node(self, value):
		parent = self.root
		while parent != None:
			if parent.value < value:
				parent = parent.right
			elif parent.value > value:
				parent = parent.left
			else:                 ## same value for two nodes cannot exist
				return False
		parent = Node(value)

	## recursion one
	def insert_node_rec(self, root, value):
		if root == None:
			root = Node(value)
		else:
		 	if root.value > value:
		 		insert_node(root.left, value)
		 	elif root.value < value:
		 		insert_node(root.right, value)
		 	else:                                   ## same values cannot exist in the BST
		 		return False

	def traverse_tree(self):
		  ## INORDER



bst = BST()
bst.insert_node(2)

