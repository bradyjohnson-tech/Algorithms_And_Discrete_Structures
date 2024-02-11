class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level


    def print_tree(self):
        print(self.get_level() * "  " + "|__" + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()


def build_product_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    root.add_child(laptop)
    laptop.add_child(TreeNode("Mac"))


    return root


if __name__ == '__main__':
    root = build_product_tree()
    root.print_tree()
    pass



    # recursive function where the child of a node will be another node