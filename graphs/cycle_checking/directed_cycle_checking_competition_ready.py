nodes = [] # Adjecncey list

n = len(nodes)
visited = [0] * n 
prev = [None] * n

for i in range(n):
    if visited[i]:
        continue
    q = [(i, 1, None)]  # (node, mode, parent)

    while q:
        u, m, p = q.pop()
        
        if m == 1:
            if visited[u] != 0:
                continue

            visited[u] = 1
            prev[u] = p

            q.append((u, 2, p))

            for v in nodes[u]:
                if visited[v] == 0:
                    q.append((v, 1, u))
                elif visited[v] == 1:
                    cycle = [u]
                    h = u
                    while h != v:
                        h = prev[h]
                        cycle.append(h)
                    cycle.append(u)
                    print("cycle:", cycle[::-1])
        else:
            visited[u] = 2
