"""
Solution1 Basic recursion
T: (2^n)
S: O(n)
"""
def fib(self, n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    return self.fib(n-1) + self.fib(n-2)

"""
Solution2 Recursion with memorization
T:O(n)
S:O(n)
"""
class Solution:
    def fib(self, n: int) -> int:
        return self.fib_mem(n, {})
    def fib_mem(self, n, mem):
        if n in mem:
            return mem[n]
        if n == 0:
            return 0
        if n == 1:
            return 1
        return self.fib_mem(n-1, mem) + self.fib_mem(n-2, mem)

"""
T: O(n)  S:O (1)
"""
def fib(self, n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n+1):
        a,b = b, a+b
    return b