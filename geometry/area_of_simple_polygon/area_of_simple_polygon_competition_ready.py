points = [(x, y)]

A = 0
for i in range(len(points) - 1):
    p1 = points[i]
    p2 = points[(i+1)]
    A += p2[1]*p1[0]-p2[0]*p1[1]
p1 = points[-1]
p2 = points[0]
A += p2[1]*p1[0]-p2[0]*p1[1]