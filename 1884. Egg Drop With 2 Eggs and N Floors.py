from functools import cache
"""
Question:minimum move to find perfect floor <= f wont break
Topic: DP topbottom with memo pick go up or go down
Step:if f break, go down, egg-1&floor-1;otherwise, keep egg&floor+1
"""
class Solution:
    def twoEggDrop(self, n: int) -> int:
        # choice go up or down
        # dp(k egg, n) = 1 + min( max ( dp(k-1, x-1), dp(k, n-x)  ) )
        # top to bottom DP dfs with memorization
        k = 2
        memo =[[0 for kp in range(k+1)] for x in range(n+1)]
        @cache
        def dp(k,x):
            if k == 1 or x <= 1:
                # only one egg try floor one by one
                return x
            if memo[x][k] > 0:
                return memo[x][k]
            res = float('inf')
            for f in range(1, x+1):
                # Take the worst-case result of:
                # 1. Egg breaks: solve for `f-1` floors with `k-1` eggs.
                # 2. Egg doesn't break: solve for `x-f` floors with `k` eggs.
                worst= max(dp(k - 1, f - 1), dp(k, x - f))
                res = min(res, 1+worst)
            # update res
            memo[x][k] = res
            return res

        return dp(2, n)
