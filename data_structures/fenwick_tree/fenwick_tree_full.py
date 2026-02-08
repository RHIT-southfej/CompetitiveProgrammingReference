class FenwickTree:
    def __init__(self, n, arr=None):
        if arr is None:
            fenwick = [0] * n
        else:
            fenwick = arr[:]
            for i in range(n):
                j = i | (i + 1)
                if j < n:
                    fenwick[j] += fenwick[i]
        self.fenwick = fenwick
        
    def prefix_sum(self, i):
        sum = 0
        while i >= 0:
            sum += self.fenwick[i]
            i = (i & (i + 1)) - 1
        return sum

    def range_sum(self, l, r):
        if l > r:
            return 0
        return self.prefix_sum(r) - (self.prefix_sum(l - 1) if l > 0 else 0)

    def add(self, i, delta):
        n = len(self.fenwick)
        while i < n:
            self.fenwick[i] += delta
            i = i | (i + 1)
          
arr = []  
fenwick = FenwickTree(len(arr), arr)

n = 0
fenwick = FenwickTree(n)