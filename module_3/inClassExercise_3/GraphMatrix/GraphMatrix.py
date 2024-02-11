class GraphMatrix:
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


if __name__ == '__main__':
    while True:
        try:
            n = int(input('Enter the number of vertices (from 2 to 5): '))
            if 2 <= n <= 5:
                graph = GraphMatrix(n)

                for _ in range(2 * n):
                    i, j, w = map(int, input("Enter the edge origin, destination, and weight (i, j, w): ").split())
                    graph.add_edge(i, j, w)
                graph.display()
                break
            else:
                print("Number of vertices must be between 2 and 5. Try again.")
        except ValueError:
            print("Invalid input. Triplets should be entered as: i j w")



