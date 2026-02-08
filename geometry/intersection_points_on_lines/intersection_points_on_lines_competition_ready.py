def o(a, b, c):
    v1 = (b[0] - a[0], b[1] - a[1])
    v2 = (c[0] - a[0], c[1] - a[1])
    return v1[0] * v2[1] - v1[1] * v2[0]

def OnSegment(pi, pj, pk):
    if min(pi[0], pj[0]) <= pk[0] <= max(pi[0], pj[0]) and min(pi[1], pj[1]) <= pk[1] <= max(pi[1], pj[1]):
        return True
    return False

def intersect(p1, p2, p3, p4):
    d1 = o(p3, p4, p1)
    d2 = o(p3, p4, p2)
    d3 = o(p1, p2, p3)
    d4 = o(p1, p2, p4)

    if ((d1 > 0 and d2 < 0) or (d1 < 0 and d2 > 0)) and \
       ((d3 > 0 and d4 < 0) or (d3 < 0 and d4 > 0)):

        A0 = p2[1] - p1[1]
        B0 = p1[0] - p2[0]
        C0 = A0 * p1[0] + B0 * p1[1]

        A1 = p4[1] - p3[1]
        B1 = p3[0] - p4[0]
        C1 = A1 * p3[0] + B1 * p3[1]

        D = A0 * B1 - A1 * B0
        x = B1 * C0 - B0 * C1
        y = A0 * C1 - A1 * C0
        return (x / D, y / D)

    pts = []
    if d1 == 0 and OnSegment(p3, p4, p1): pts.append(p1)
    if d2 == 0 and OnSegment(p3, p4, p2): pts.append(p2)
    if d3 == 0 and OnSegment(p1, p2, p3): pts.append(p3)
    if d4 == 0 and OnSegment(p1, p2, p4): pts.append(p4)

    if not pts:
        return None

    pts = sorted(set(pts))
    if len(pts) == 1:
        return pts[0]
    else:
        return (pts[0][0], pts[0][1], pts[-1][0], pts[-1][1])

ans = intersect(p1,p2,p3,p4)
# ans = None -> no intersect
# len(ans) = 2 -> single ponint
# len(ans) = 4 -> segment of intersection