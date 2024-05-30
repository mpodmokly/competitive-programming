# Breadth-first search algorithm

from queue import Queue

def bfs(G, s):
    n = len(G)
    visited = [False] * n
    visited[s] = True
    parent = [-1] * n
    d = [-1] * n
    d[s] = 0

    Q = Queue()
    Q.put(s)

    while not Q.empty():
        v = Q.get()
        for i in range(len(G[v])):
            if not visited[G[v][i]]:
                d[G[v][i]] = d[v] + 1
                parent[G[v][i]] = v
                visited[G[v][i]] = True
                Q.put(G[v][i])

    return d, parent
