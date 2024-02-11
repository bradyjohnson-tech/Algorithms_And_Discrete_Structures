class BinarySearchTree:
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
        if self.left:
            self.left.in_order_traversal()
        print(self.data)
        if self.right:
            self.right.in_order_traversal()

    def pre_order_traversal(self):
        print(self.data)
        if self.left:
            self.left.pre_order_traversal()
        if self.right:
            self.right.pre_order_traversal()

    # def post_order_traversal(self):
    #     if self.right:
    #         self.right.post_order_traversal()


    def search(self, data):
        if data == self.data:
            return True
        if data < self.data:
            if self.left:
                return self.left.search(data)
            else:
                return False
        else:
            if self.right:
                return self.right.search(data)
            else:
                return False





def build_tree(elements):
    root = BinarySearchTree(elements[0])
    for i in range(1, len(elements)):
        root.add_child(elements[i])
    return root

if __name__ == '__main__':
    # numberTree = [17,4,1,20,9,23,18,34]
    # build_tree(numberTree).in_order_traversal()
    # build_tree(numberTree).pre_order_traversal()
    # build_tree(numberTree).post_order_traversal()
    # print(build_tree(numberTree).search(21))


    countries = ['Brazil', 'Germany', 'india', 'Sweden']
    build_tree(countries)
    build_tree(countries).in_order_traversal()
    print(build_tree(countries).search('india'))
