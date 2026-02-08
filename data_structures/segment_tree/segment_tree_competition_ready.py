def build(arr, n):
    tree = [0] * (2 * n)
    for i in range(n): 
        tree[n + i] = arr[i] 
    for i in range(n - 1, 0, -1): 
        tree[i] = max(tree[i << 1], tree[i << 1 | 1])
    return tree

def update(p, v, n):
    tree[p + n] = v 
    p = p + n 
    i = p
    while i > 1:
        tree[i >> 1] = max(tree[i], tree[i ^ 1])
        i >>= 1 

def query(l, r, n):
    res = float('-inf') # -inf for max, inf for min, 0 for sum
    l += n
    r += n + 1
    while l < r:
        if (l & 1):
            res = max(res, tree[l])
            l += 1
        if (r & 1):
            r -= 1
            res = max(res, tree[r])
        l >>= 1
        r >>= 1
    return res 

arr = []
n = len(arr)
tree = build(arr, n)