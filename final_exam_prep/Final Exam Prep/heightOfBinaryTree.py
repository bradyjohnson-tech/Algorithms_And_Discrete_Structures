class Node:
    def __init__(self,d):
        self.data = d
        self.Left = None
        self.Right = None

def heightTree(node):
    if node is None:
        return -1
    else:
        left_height = heightTree(node.Left)
        right_height = heightTree(node.Right)
        if left_height < right_height:
            return right_height + 1
        else:
            return left_height + 1

# O(log(n))

# Worst case:
# ● T(n) = 2 T(n-1) + 1 Best case:
# ● T(n) = 2T(n/2) + 1
