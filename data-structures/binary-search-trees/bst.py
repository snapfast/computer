# bst has


class Node:
    def __init__(self, value):
        self.left = None
        self.value = value
        self.right = None


class BST:
    def __init__(self):
        self.root = None  # Initialize root as an instance variable

    # iterative insertion
    def insert_node(self, new_value):
        new_node = Node(new_value)
        if self.root is None:
            self.root = new_node
            return

        current = self.root
        while True:
            if new_value < current.value:
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left
            elif new_value > current.value:
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right
            else:
                # Value already exists
                return False

    def _insert_rec(self, current_node, new_value):
        """
        Private helper function for recursive insertion.
        Returns the root of the subtree after insertion.
        """
        if current_node is None:
            return Node(new_value)

        if new_value < current_node.value:
            current_node.left = self._insert_rec(current_node.left, new_value)
        elif new_value > current_node.value:
            current_node.right = self._insert_rec(current_node.right, new_value)
        elif new_value == current_node.value:
            print("value is a duplicate")

        return current_node  # Return the current node (the root of this subtree)

    def insert_node_rec(self, new_value):
        self.root = self._insert_rec(self.root, new_value)
        return True
    
	# delete the node - recursive version - does not work at the moment
    def delete(self, delete_value):
        current = self.root
        while delete_value != current.value:
            print(current.value)
            if delete_value < current.value:
                current = current.left
            else:
                current = current.right
        print(current.value, current.left, current.right)
        if current.right != None:
            current = current.right
        else:
            current = current.left

    # in-order traversal
    def in_order_traversal(self, start):
        if start:
            self.in_order_traversal(start.left)
            print(start.value, end="-")
            self.in_order_traversal(start.right)

    # public in-order traversal
    def print_in_order(self):
        print("in order traversal")
        self.in_order_traversal(self.root)
        print(" ")

    # pre-order traversal
    def pre_order_traversal(self, start):
        if start:
            print(start.value, end="-")
            self.pre_order_traversal(start.left)
            self.pre_order_traversal(start.right)

    # public pre-order traversal
    def print_pre_order(self):
        print("pre order traversal")
        self.pre_order_traversal(self.root)
        print(" ")

    # height of bst
    def height(self):
        print("fdsa")
        start = self.root


# Test Execution
bst = BST()
bst.insert_node(30)
bst.insert_node_rec(70)
bst.insert_node(50)
bst.insert_node(20)
bst.insert_node(40)
bst.print_in_order()
bst.print_pre_order()
bst.delete(50)
bst.print_in_order()
bst.print_pre_order()
# Output will be: 2, 3, 4, 5
