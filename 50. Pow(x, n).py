class Solution:
    """
    50. Pow(x, n) 
    """
    def myPow(self, x: float, n: int) -> float:
        # 1SOLUTION
        power = 1
        sign = 1
        if n < 0: sign = -1
        n = abs(n)
        for _ in range(n):
            power = power * x
        return power if sign == 1 else 1 / power
        # 2SOLUTION Divide and conquer logn
        # divide problem to subproblem, conquer handle base case, merged to result
        # x^n= x^n/2 * x^n/2 when n is even
        # x^n= x^(n+1)/2 * x^(n-1)/2 when n is odd
        def pow(y, m):
            if m == 0:
                return 1
            half = pow(y, m//2)
            if m % 2 == 0:
                return half * half
            else:
                return half*half*y

        # base case
        if x == 0 or n == 1: 
            return x
        if n < 0:
            return 1/pow(x, -n)
        # recursion
        # return pow(x, n)
        # 3SOLUTION: BIT logn
        """
        x=2,n=13(1101)
        n2=1101,res=2,x=4
        n2=110, res=2,x=16
        n2=11,  res=32, x=256
        ...
        n2=1
        """
        res = 1
        n2=abs(n)
        while n2 > 0:
            # check n2 least significant(rightmost) bit is 1
            if n2&1:
                res *= x
            x *= x
            # shift right 
            n2 >>=1
        return res if n >= 0 else 1/res






