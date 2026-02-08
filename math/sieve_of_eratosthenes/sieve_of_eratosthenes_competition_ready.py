def sieve(n):
    if n < 2:
        return []

    is_prime = [True] * ((n // 2) + 1)
    is_prime[0] = False  # 1 is not prime

    for i in range(3, int(n**0.5) + 1, 2):
        if is_prime[i // 2]:
            for j in range(i * i, n + 1, 2 * i):
                is_prime[j // 2] = False

    primes = [2] + [2 * i + 1 for i in range(1, n // 2 + 1) if is_prime[i]]
    return primes

# 10^7 takes ~0.5 seconds
primes = sieve(n)