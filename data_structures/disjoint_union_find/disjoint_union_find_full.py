'''
Given n disjoint elements, a Disjoint Union Find data structure keeps track of the partition of the equivalence class on the elements. It supports two operations.

Union(a, b): Merge the set containing a with the set containing b.

Find(a): Find the representative of the set containing a and compress the sets.

Initially, each element's representative is itself. When two sets are merged, one set's representative becomes the representative of the other set. This way, we can determine if two elements are in the same set by determining if they have the same representative.

Input:
int n - the number of sets

Disjoint Sets: two sets are disjoint if their intersection is empty.
Representaive: an element of a set identifies the set.
'''
def union(a, b):
    representative_a = find(a)
    representative_b = find(b)
    
    if representative_a == representative_b:
        return
    elif rank[representative_a] > rank[representative_b]:
        sets[representative_b] = representative_a
    elif rank[representative_a] < rank[representative_b]:
        sets[representative_a] = representative_b
    else:
        sets[representative_b] = representative_a
        rank[representative_a] += 1

def find(a):
    if a != sets[a]:
        sets[a] = find(sets[a])
    return sets[a]

'''
End of code DSU-specific code.

Kattis: https://open.kattis.com/problems/unionfind

Test Case:

Input:
10 4
? 1 3
= 1 8
= 3 8
? 1 3

Expected Output:
no
yes

Start of test code.
'''
import sys

n, q = map(int, input().split())

sets = [i for i in range(n)]
rank = [0] * n

lines = sys.stdin.read().splitlines()

output = []

for line in lines:
    command, a, b = line.split()
    a, b = int(a), int(b)
    if command == "=":
        union(a, b)
    elif command == "?":
        representative_a = find(a)
        representative_b = find(b)
        output.append("yes") if representative_a == representative_b else output.append("no")

print("\n".join(output))