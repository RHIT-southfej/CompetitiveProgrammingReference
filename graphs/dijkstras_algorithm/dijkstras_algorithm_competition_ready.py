import heapq

def dijkstra(s):
    n = len(nodes)
    inf = float('inf')
    dist = [inf] * n
    # prev = [None] * n
    dist[s] = 0

    pq = [(0, s)]

    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue

        for v, w in nodes[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                # prev[v] = u
                heapq.heappush(pq, (nd, v))

    return dist #, prev

nodes = [[(v, w), (v, w)], [(v, w)]] # Adjecncey list
dists = dijkstra(s)