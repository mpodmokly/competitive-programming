# Edmonds-Karp algorithm finds the maximum flow in
# a flow network

from queue import Queue

def bfs(G, R, s):
    n = len(G)
    visited = [False] * n
    d = [-1] * n
    parent = [-1] * n

    visited[s] = True
    d[s] = 0
    Q = Queue()
    Q.put(s)

    while not Q.empty():
        u = Q.get()
        for i in range(len(G[u])):
            if R[u][G[u][i]] > 0 and not visited[G[u][i]]:
                visited[G[u][i]] = True
                d[G[u][i]] = d[u] + 1
                parent[G[u][i]] = u
                Q.put(G[u][i])
    
    return parent

def min_flow_bfs(R, path, t):
    curr = t
    min_flow = R[path[curr]][curr]

    while path[curr] != -1:
        if R[path[curr]][curr] < min_flow:
            min_flow = R[path[curr]][curr]
        
        curr = path[curr]

    return min_flow

def edmonds_karp(G):
    n = len(G)

    F = [[0] * n for _ in range(n)]
    R = [[0] * n for _ in range(n)]
    s = 0
    t = n - 1

    for i in range(n):
        for j in range(len(G[i])):
            R[i][G[i][j][0]] += G[i][j][1]
            R[G[i][j][0]][i] += G[i][j][1]

    while True:
        path = bfs(G, R, s)
        
        if path[t] == -1:
            break

        a = min_flow_bfs(R, path, t)
        curr = t

        while path[curr] != -1:
            F[path[curr]][curr] += a
            F[curr][path[curr]] -= a
            R[path[curr]][curr] -= a
            R[curr][path[curr]] += a

            curr = path[curr]
    
    max_flow = 0
    for i in range(n):
        max_flow += F[0][i]
    
    return max_flow
