# Algorithm finds bridges in a graph using "low" function

def dfs(G, s, visited, time, d, low, parent, bridges):
    visited[s] = True
    time[0] += 1
    d[s] = time[0]
    low[s] = time[0]
    
    for i in range(len(G[s])):
        if not visited[G[s][i]]:
            dfs(G, G[s][i], visited, time, d, low, s, bridges)
            low[s] = min(low[s], low[G[s][i]])
        elif G[s][i] != parent:
            low[s] = min(low[s], low[G[s][i]])
    
    if (low[s] == d[s] and parent != -1):
        bridges.append([s, parent])

def find_bridges(G):
    n = len(G)
    visited = [False] * n
    d = [0] * n
    low = [0] * n
    bridges = []

    for i in range(n):
        if not visited[i]:
            dfs(G, i, visited, [0], d, low, -1, bridges)
    return bridges
