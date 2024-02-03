"""
    Questions: factor of N
"""
def kthFactor(self, n: int, k: int) -> int:
    # return list of factors of n
    f = []
    factor = 1
    # largest factor <= n/2
    while factor <= n//2:
        if n % factor == 0: # it is factor
            f.append(factor)
        factor += 1
    f.append(n)
    return -1 if len(f) < k else f[k-1]
        