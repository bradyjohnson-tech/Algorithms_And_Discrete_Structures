class AdjacencyMatrix:
    def __init__(self, n):
        self.n = n
        self.matrix = [([0] * n) for _ in range(n)]

    def add_edge(self, i, j, w):
        if i >= self.n or j >= self.n:
            print("Invalid vertex index")
            return
        self.matrix[i][j] = w

    def display(self):
        for i in range(self.n):
            for j in range(self.n):
                print(self.matrix[i][j], end=' ')
            print()

    def add_abs_edge(self, binaryTree):
        for i in range(self.n):
            for j in range(self.n):
                self.matrix[i][j] += binaryTree[i][j]

