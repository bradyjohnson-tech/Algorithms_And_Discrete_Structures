import utils
import binaryTree
import graph


def read_vector_from_file(filename='numbers.txt'):
    # Read numbers from a file into a vector of integers
    with open(filename, 'r') as file:
        a = [int(line.strip()) for line in file]
    return a

d = {}

# function to create adjacency matrix of tree
def create_adjacency_matrix(root, matrix):
    # if root is None, return
    if root is None:
        return

    # if left child exists
    if root.left is not None:
        # set weight of edge as absolute difference of data of root and left child
        matrix[d[root.data]][d[root.left.data]] = abs(root.data - root.left.data)
        # recursively call function for left child
        create_adjacency_matrix(root.left, matrix)

    # if right child exists
    if root.right is not None:
        # set weight of edge as absolute difference of data of root and right child
        matrix[d[root.data]][d[root.right.data]] = abs(root.data - root.right.data)
        # recursively call function for right child
        create_adjacency_matrix(root.right, matrix)

    # return adjacency matrix
    return matrix


def inorder_traversal(root):
    # if root is None, return
    if root is None:
        return

    d[root.data] = len(d)
    inorder_traversal(root.left)
    inorder_traversal(root.right)

# print(read_vector_from_file())
# utils.generate_non_repeating_vector_and_save(16)

if __name__ == '__main__':
    numbers = [34, 12, 8, 13, 55]
    binary_tree = binaryTree.BinaryTree.build_tree(numbers)

    inorder_traversal(binary_tree)

    graph = []
    for i in range(len(numbers)):
        graph.append([])
        for j in range(len(numbers)):
            graph[i].append(0)

    graph = create_adjacency_matrix(binary_tree, graph)

    for i in range(len(graph)):
        print(graph[i])
