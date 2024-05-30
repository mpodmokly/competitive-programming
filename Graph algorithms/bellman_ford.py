# Bellman-Ford algorithm finds the shortests paths in a weighted
# graph, with negative weights of edges, but in the graph can not
# be any negative cycle

def bellman_ford(G, s):
    n = len(G)
    d = [float('inf')] * n
    parent = [None] * n
    d[s] = 0

    for i in range(n - 1):
        for j in range(n):
            for k in range(len(G[j])):
                if d[G[j][k][0]] > d[j] + G[j][k][1]:
                    d[G[j][k][0]] = d[j] + G[j][k][1]
                    parent[G[j][k][0]] = j
    
    for i in range(n):
        for j in range(len(G[i])):
            if d[G[i][j][0]] > d[i] + G[i][j][1]:
                return False # NEGATIVE CYCLE
    
    return d
