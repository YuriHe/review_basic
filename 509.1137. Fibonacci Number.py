# """
# Solution1 Basic recursion
# T: (2^n)
# S: O(n)
# """
def fib(self, n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    return self.fib(n-1) + self.fib(n-2)

# """
# Solution2 Recursion with memorization
# T:O(n)
# S:O(n)
# """
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
        mem[n] = self.fib_mem(n-1, mem) + self.fib_mem(n-2, mem)
        return mem[n]

# """
# T: O(n)  S:O (1) (Best)
# """
def fib(self, n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n+1):
        a,b = b, a+b
    return b

"""
Python iterator class
"""
class Fibonacci():
    def __init__(self, max):
        self.max = max
        self.a = 0
        self.b = 1
        # track how many numbers generated
        self.ctn = 0 

    def __iter__(self): # This method makes the class an iterator, allowing you to use it in a for loop.
        # return terator object itself
        return self
    
    def __next__(self):
        if self.ctn < self.max:
            fib = self.a # save it for return cur v
            self.a, self.b = self.b, self.a + self.b
            self.ctn += 1
            return fib
        else:
            raise StopIteration

fib = Fibonacci(20)
for n in fib:
    print(n)

"""
Python generator function with yield
"""
def get_fib():
    a, b = 0, 1
    while True:
        yield a # return cur v
        a,b = b, a+b

# create generator function
fib = get_fib()
# iterate and printout
for _ in range(3):
    print(next(fib))


class Solution:
    """
    1137. N-th Tribonacci Number
    T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
    """
    # SOLUTION1 recursion with memorization
    def tribonacci(self, n: int) -> int:
        # recursion
        return self.rec(n, {})

    def rec(self,n, mem):
        if n in mem:
            return mem[n]
        
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        mem[n] = self.rec(n-2, mem) + self.rec(n-1, mem) + self.rec(n-3, mem)
        return mem[n]

    # SOLUTION2: DP bottom up
    def tribonacci(self, n: int) -> int:
        if n <= 1:
            return n
        dp = [0] * (n+1)
        # base 
        dp[0] = 0
        dp[1] = 1
        dp[2] = 1

        for i in range(3, n+1):
            dp[i] = dp[i-3] + dp[i-2] + dp[i-1]
        return dp[n]
