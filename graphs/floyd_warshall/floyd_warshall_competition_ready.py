# adjacency matrix
def floyd_warshall(graph):
    n = len(graph)
    inf = float('inf')

    for k in range(n):
        for i in range(n):
            if graph[i][k] == inf:
                continue
            for j in range(n):
                if graph[k][j] == inf:
                    continue
                nd = graph[i][k] + graph[k][j]
                if nd < graph[i][j]:
                    graph[i][j] = nd

    neg = [graph[i][i] < 0 for i in range(n)]

    for k in range(n):
        if not neg[k]:
            continue
        for i in range(n):
            if graph[i][k] == inf:
                continue
            for j in range(n):
                if graph[k][j] != inf:
                    graph[i][j] = -inf