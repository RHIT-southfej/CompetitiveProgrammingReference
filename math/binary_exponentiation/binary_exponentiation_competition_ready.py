# For numbers
pow(a, b)

# For numbers mod m
pow(a, b, m)

# For non number multiplication
def fast_pow(a, b):
    if b == 0:
        return id
    if b == 1: 
        return a
    h = fast_pow(mult(a, a), b // 2)
    if b & 1: 
        return mult(a, h)
    return h