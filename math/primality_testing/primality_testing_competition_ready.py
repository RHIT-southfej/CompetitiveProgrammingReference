import random

def is_prime(n):
    if n < 2:
        return False
    if n in (2,3):
        return True
    if n % 2 == 0:
        return False

    for i in range(3, min(n, 102), 2):
        if n % i == 0:
            return False

    for _ in range(50):
        base = random.randint(2, n - 2)
        
        k = n - 1
        m = 0
        while k % 2 == 0:
            k //= 2
            m += 1

        a = pow(base, k, n)
        if a == 1 or a == n - 1:
            continue

        for _ in range(m - 1):
            a = pow(a, 2, n)
            if a == n - 1:
                break
        else:
            return False
    return True