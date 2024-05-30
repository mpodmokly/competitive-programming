# Depth-first search algorithm

def dfs(G, s, visited):
    visited[s] = True

    for i in range(len(G[s])):
        if not visited[G[s][i]]:
            dfs(G, G[s][i], visited)
