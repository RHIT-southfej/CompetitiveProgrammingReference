def range_sum(i, j):
    return sum(j) - sum(i - 1)

def sum(i):
    i = i+1
    sum = 0
    while i > 0:
        sum += fenwick[i - 1]
        i = i & (i - 1)
    return sum

def add(i, value):
    while i < len(fenwick):
        fenwick[i] += value
        i = i | (i + 1)
        
def build_tree():
    n = len(arr) - 1
    for i in range(1, n+2):
        fenwick[i - 1] += arr[i - 1]
        if i + (i & -i) - 1 <= n:
            fenwick[i + (i & -i) - 1] += fenwick[i - 1]
            
def force(i,j):
    a = 0
    for i in range(i,j+1):
        a += arr[i]
    return a
            
arr = []
fenwick = [0] * len(arr)
build_tree()