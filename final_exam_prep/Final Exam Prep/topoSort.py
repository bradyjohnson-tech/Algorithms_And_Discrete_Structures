def topoSort(V, E, A):
    size = len(A)
    for v in range(len(V)):
        if v not in A:
            for e in E:
                if(v == e[1]) and (e[0] not in A):
                    break
                else:
                    A.append(V)
                    break
                continue
        if len(A) == size:
            return False                # stop condition not DAG
        elif len(V) == len(A):
            return True
        else:
            return topoSort(V, E, A)     # do another recursive call



V = ["A", "B", "C", "D","E", "F", "G", "H", "I", "J","K"]
E = [(0, 1), (0, 2), (1, 3), (2, 3), (3, 4), (4, 5)]
A = []
if (topoSort(V, E, A)):
    print("Topological sorting found:")
    for a in A:
        print(V[a], end="")
    print()
else:
    print("The graph is not a DAG!")

# O(n*m)
