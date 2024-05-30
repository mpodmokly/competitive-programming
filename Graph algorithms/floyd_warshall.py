# Floyd-Warshall algorithm finds the shortests paths between each
# pair of vertices in a weighted graph, accepts negative weights
# of edges, but in the graph can not be any negative cycle

def floyd_warshall(G):
    n = len(G)
    d = [[float('inf')] * n for item in range(n)]
    parent = [[None] * n for item in range(n)]
    for i in range(n):
        d[i][i] = 0

    for i in range(n):
        for j in range(len(G[i])):
            d[i][G[i][j][0]] = G[i][j][1]
            parent[i][G[i][j][0]] = i
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if d[i][j] > d[i][k] + d[k][j]:
                    d[i][j] = d[i][k] + d[k][j]
                    parent[i][j] = parent[k][j]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if d[i][j] > d[i][k] + d[k][j]:
                    return False
    
    return d, parent
