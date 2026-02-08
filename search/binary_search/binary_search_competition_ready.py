error = pow(10, -9)
while h - l > error:
    m = (l + h) / 2
    if func(m):
        h = m
    else:
        l = m
ans = l
