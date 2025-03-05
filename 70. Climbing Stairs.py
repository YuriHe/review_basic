class Solution:
    def climbStairs(self, n: int) -> int:
        """
        SOLUTION1:bottom-top DP
        STEP:dp[i]=dp[i-1]+dp[i-2] means total distinc way at i 
        TIME:O(n) SPACE: O(n)
        """
        # bottom to top, 求多少组合方式
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, len(dp)):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]