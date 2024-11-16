class Solution:
    """
    Question: get mini cost for climbing stairs, you can choose either climb one or two steps, and start from index 0 or index 1
    Goal use minimum total cost to reach top of floor
    Choice start index 0 or 1, use 1 or 2 steps
    Rule dp[n] : get mini cost by choosing steps, in the end, compare dp[n-1] and dp[n-2] different starting point
    """
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # define dp, default cost = 0(impossible value)
        l = len(cost)
        dp = [0] * (l)
        # start index0
        dp[0] = cost[0]
        # start index1
        dp[1] = cost[1]
        # 1,2,3 > 2
        for i in range(2, l):
            # choose min cost from pre step, or pre-pre step then + cost, to get updated min cost for this point
            dp[i] = min(dp[i-2],dp[i-1]) + cost[i]

        return min(dp[l-1],dp[l-2]) # dp[l-2] mean no cost to reach last, dp[l-1] comes from previous second step