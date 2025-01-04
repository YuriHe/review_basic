from functools import cache

class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        # choice go up or down
        # dp(k egg, n) = 1 + min( max ( dp(k-1, x-1), dp(k, n-x)  ) )
        # top to bottom DP dfs with memorization
        memo =[[0 for kp in range(k+1)] for x in range(n+1)]
        @cache
        def dp(k,x):
            if k == 1 or x <= 1:
                # only one egg try floor one by one
                return x
            if memo[x][k] > 0:
                return memo[x][k]
            res = float('inf')
            low, high = 1, x+1
            while low <= high:
                mid = low + (high-low)//2
                left = dp(k-1, mid-1)
                right =dp(k,x-mid)
                res = min(res, 1+max(left,right))
                if left == right:
                    break
                elif left < right: # more steps go up
                    low = mid+1
                else:
                    high = mid-1

            # update res
            memo[x][k] = res
            return res

        return dp(k, n)
