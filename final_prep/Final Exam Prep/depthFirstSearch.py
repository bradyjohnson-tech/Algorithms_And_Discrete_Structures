def DFS(V, E):
    def _visit(i, count):
        for e in E:
            if(e[0] == i) and (V[e[1]] == -1):
                count = _visit(e[1], count)
            elif(e[1] == i) and (V[e[0]] == -1):
                count = _visit(e[0], count)
        return count

    for i in range(len(V)):
        V[i] = -1
    count = 0
    for i in range(len(V)):
        if (V[i] == -1):
            count = _visit(i, count)

# Big-oh of O(n*m)

