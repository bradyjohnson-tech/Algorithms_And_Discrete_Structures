import binaryTree


def read_vector_from_file(filename='numbers.txt'):
    # Read numbers from a file into a vector of integers
    with open(filename, 'r') as file:
        a = [int(line.strip()) for line in file]
    return a


dictionary = {}


def adjacency_matrix(bt, graph):
    if bt is None:
        return

    if bt.left is not None:
        graph[dictionary[bt.data]][dictionary[bt.left.data]] = abs(
            bt.data - bt.left.data)
        adjacency_matrix(bt.left, graph)

    if bt.right is not None:
        graph[dictionary[bt.data]][dictionary[bt.right.data]] = abs(
            bt.data - bt.right.data)
        adjacency_matrix(bt.right, graph)

    return graph


def pre_order_traversal(binary_tree):
    if binary_tree is None:
        return

    dictionary[binary_tree.data] = len(dictionary)
    if binary_tree.left:
        pre_order_traversal(binary_tree.left)
    if binary_tree.right:
        pre_order_traversal(binary_tree.right)


# utils.generate_non_repeating_vector_and_save(16)

if __name__ == '__main__':
    numbers = read_vector_from_file()
    binary_tree = binaryTree.BinaryTree.build_tree(numbers)

    pre_order_traversal(binary_tree)

    graph = []
    for i in range(len(numbers)):
        graph.append([])
        for j in range(len(numbers)):
            graph[i].append(0)

    graph = adjacency_matrix(binary_tree, graph)

    for i in range(len(graph)):
        print(graph[i])
