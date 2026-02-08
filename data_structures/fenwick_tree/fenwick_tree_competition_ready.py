def build_tree(arr):
    n = len(arr)
    fenwick = arr[:]
    for i in range(n):
        j = i | (i + 1)
        if j < n:
            fenwick[j] += fenwick[i]
    return fenwick

def prefix_sum(i):
    s = 0
    while i >= 0:
        s += fenwick[i]
        i = (i & (i + 1)) - 1
    return s

def range_sum(l, r):
    if l > r:
        return 0
    return prefix_sum(r) - (prefix_sum(l - 1) if l > 0 else 0)

def add(i, v):
    n = len(fenwick)
    while i < n:
        fenwick[i] += v
        i = i | (i + 1)
            
arr = []
fenwick = build_tree(arr)