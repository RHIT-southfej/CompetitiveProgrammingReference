from collections import deque

nodes = [] # Adjecncey list

q = deque([s])
been_to = [0] * len(nodes)
been_to[s] = 1

while len(q):
    u = q.popleft()
    
    # process node here
    
    for v in nodes[u]:
        if not been_to[v]:
            been_to[v] = 1
            q.append(v)