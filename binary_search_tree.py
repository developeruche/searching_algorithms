""" This is a more efficent way of searching through an array of number of even String """

class BinarySearchTree():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTree(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTree(data) 

    def in_order_traversal(self):
        element = []

        if self.left:
            element += self.left.in_order_traversal()

        element.append(self.data)

        if self.right:
            element += self.right.in_order_traversal()

    def build_tree(elements):
        root = BinarySearchTree(elements[0])

        for i in range(1, len(elements)):
            root.add_child(elements[i])
