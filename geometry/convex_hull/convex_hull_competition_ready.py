from functools import cmp_to_key

def o(a, b, c):
    if a == b:
        return 1
    if a == c:
        return -1
    v1 = (b[0] - a[0], b[1] - a[1])
    v2 = (c[0] - a[0], c[1] - a[1])
    return v1[0] * v2[1] - v1[1] * v2[0]

def convex_hull(points):
    n = len(points)
    if n <= 1:
        return points
    p0 = min(points, key=lambda p: (p[1], p[0]))
    def compare(p1, p2):
        val = o(p0, p1, p2)
        if val != 0:
            return -val
        return (p0[0] - p1[0])**2 + (p0[1] - p1[1])**2 - (p0[0] - p2[0])**2 - (p0[1] - p2[1])**2
    pts = sorted(points, key=cmp_to_key(compare))
    print(p0, pts)
    hull = []
    for p in pts:
        while len(hull) >= 2 and o(hull[-2], hull[-1], p) <= 0:
            hull.pop()
        hull.append(p)
    return hull

points = [(x, y)] # unique
hull = convex_hull(points)