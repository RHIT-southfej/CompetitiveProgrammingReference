error = 1e-9

while h - l > error:
    m1 = l + (h - l) / 3
    m2 = h - (h - l) / 3

    if func(m1) < func(m2):
        l = m1
    else:
        h = m2

ans = (l + h) / 2