class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        SOLUTION1: bottom top DP
        STEP:choose where start index 0 or index 1; then choose one jump or two jump, 
        can reach last index or more than last index
        DP[i]means minimum cost when jump at i 
        TIME SPACE: O(n)
        """
        n = len(cost)
        # choose overflow val
        dp = [1000] * n
        # initial start point
        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2,n):
            dp[i] = min(dp[i-2], dp[i-1]) + cost[i]
        
        # end point diff, dp[n-1] reach last from previous jumps, dp[n-2] can do two jump without cost
        return min(dp[n-1], dp[n-2])