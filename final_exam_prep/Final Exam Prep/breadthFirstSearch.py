def BFS(V, E):
    for i in range(len(V)):
        V[i] = -1
    count = 0
    for i in range(len(V)):
        if (V[i] == -1):
            Q = [i]
            V[i], count = count, count + 1
            while (len(Q) != 0):
                for e in E:
                    if e[0] == Q[0] and (V[e[1]] == -1):
                        Q.append(e[1])
                        V[e[1]] = count
                    elif e[1] == Q[0] and V[e[0]] == -1:
                        Q.append(e[0])
                        V[e[0]], count == count, count + 1
                Q.pop(0)


# So, the time complexity of this particular algorithm would be O(|V|*|E|).or O(n*m)

V = ["A", "B", "C", "D", "E", "F", "G"]
E = [[0, 1, 0, 1, 0, 0, 0],
     [1, 0, 1, 0, 0, 0, 1],
     [1, 1, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 1, 1, 0],
     [0, 0, 0, 0, 0, 1, 0],
     [0, 1, 0, 0, 0, 0, 0],
     [0, 0, 1, 0, 0, 1, 0]]

BFS(V, E)
print(V)
