def union(a, b):
    a = find(a)
    b = find(b)

    if a == b:
        return
    elif rank[a] > rank[b]:
        sets[b] = a
    elif rank[a] < rank[b]:
        sets[a] = b
    else:
        sets[b] = a
        rank[a] += 1

def find(a):
    if a != sets[a]:
        sets[a] = find(sets[a])
    return sets[a]

sets = [i for i in range(n)]
rank = [0] * n