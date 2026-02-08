def bellman_ford(s):
    n = len(nodes)
    inf = float('inf')
    dist = [inf] * n
    dist[s] = 0
    # prev = [None] * n
    
    for _ in range(n - 1):
        for u in range(n):
            for v, w in nodes[u]:
                if dist[u] != inf and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    # prev[v] = u
    for u in range(n):
        for v, w in nodes[u]:
            if dist[u] != inf and dist[u] + w < dist[v]:
                dist[v] = -inf
                # prev[v] = u
    changed = True
    while changed:
        changed = False
        for u in range(n):
            if dist[u] == -inf:
                for v, _ in nodes[u]:
                    if dist[v] != -inf:
                        dist[v] = -inf
                        changed = True
    return dist #, prev

nodes = [[(v, w), (v, w)], [(v, w)]] # Adjecncey list
dists = bellman_ford(s)