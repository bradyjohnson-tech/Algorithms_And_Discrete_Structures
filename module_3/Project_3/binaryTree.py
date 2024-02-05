class BinaryTree:
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
                self.left = BinaryTree(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinaryTree(data)

    def build_tree(elements):
        root = BinaryTree(elements[0])
        for i in range(1, len(elements)):
            root.add_child(elements[i])
        return root



    # def pre_order_traversal(self):
    #     print(self.data)
    #     if self.left:
    #         self.left.pre_order_traversal()
    #     if self.right:
    #         self.right.pre_order_traversal()



    # def number_of_nodes(self, node):
    #     if node is None:
    #         return 0
    #     else:
    #         return 1 + self.number_of_nodes(node.left) + self.number_of_nodes(node.right)
    #
    # def count_nodes(self):
    #     return self.number_of_nodes(self)