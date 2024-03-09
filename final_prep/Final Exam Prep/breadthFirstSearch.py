def BFS(V, E):
    for i in range(len(V)):
        V[i] = -1       # All vertices not visited
    count = 0
    for i in range(len(V)):     # for all possible cources
        if(V[i] == -1):
            Q = [i]                         # enqueue the source
            V[i], count = count, count+1    # visit it
            while(len(Q) != 0):             # for all enqueued
                for e in E:
                    if e[0] == Q[0]:         # if the edge starts at the current vertex
                            if V[e[1]] == -1:   # if the destination vertex is not visited
                                Q.append(e[1])  # enqueue the destination vertex
                                V[e[1]] = count # visit the destination vertex
                        elif e[1] == Q[0]:      # if the edge ends at the current vertex
                            if V[e[0]] == -1:   # if the source vertex is not visited
                                Q.append(e[0])  # enqueue the source vertex
                                V[e[0]] = count # visit the source vertex
                    Q.pop(0)                    # dequeue the current vertex

# So, the time complexity of this particular algorithm would be O(|V|*|E|).or O(n*m)
