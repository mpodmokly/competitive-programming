# Kruskal's algorithm finds minimum spanning tree (MST) in a graph
# using Disjoint Set Union

def key(x):
    return x[2]

def find(T, x):
    if T[x] == x:
        return x
    T[x] = find(T, T[x])
    return T[x]

def union(T, size, x, y):
    x = find(T, x)
    y = find(T, y)

    if x == y:
        return
    if size[x] > size[y]:
        size[x] += size[y]
        T[y] = x
    else:
        size[y] += size[x]
        T[x] = y

def kruskal(G):
    n = len(G)
    edges = []
    
    for i in range(n):
        for j in range(len(G[i])):
            if i < G[i][j][0]:
                edges.append([i, G[i][j][0], G[i][j][1]])
    
    edges.sort(key=key)
    mst = []
    rep = [i for i in range(n)]
    size = [1] * n

    for i in range(len(edges)):
        if find(rep, edges[i][0]) != find(rep, edges[i][1]):
            mst.append(edges[i])
            union(rep, size, edges[i][0], edges[i][1])

    return mst
