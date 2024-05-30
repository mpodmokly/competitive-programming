# Dijkstra algorithm finds the shortests paths in a weighted graph

from queue import PriorityQueue

def dijkstra(G, s):
    n = len(G)
    d = [float('inf')] * n
    d[s] = 0
    parent = [-1] * n

    Q = PriorityQueue()
    Q.put([0, s])
    
    while not Q.empty():
        u = Q.get()[1]

        for i in range(len(G[u])):
            if d[G[u][i][0]] > d[u] + G[u][i][1]:
                d[G[u][i][0]] = d[u] + G[u][i][1]
                parent[G[u][i][0]] = u

                Q.put([d[G[u][i][0]], G[u][i][0]])
    
    return d, parent
