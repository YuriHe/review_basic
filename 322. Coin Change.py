class Solution:
    """
    Question: return fewest number of coins to make up that amount
    Greedy -> Not work since minimum steps 
    DFS - Backtracking: make tree break into subproblem top-bottom dp mem
    Now use bottom-up dp 1D -> minimum + combinations/choices 
    eg. 
    coints = [1,2,5], amount: 4
    dp[cur_amount]=min coins number
    dp[0]=0, dp[1]=1 dp[2]=1(min(dp[2], 1+dp[2-1])=2 , min(dp[2], 1+dp[2-2])=1)
    """
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        SOLUTION1: bottom top 1D DP
        TIME: O(n*m) n is amount, m is number of coins
        SPACE: O(n) n is amount 
        IDEA:create dp size is amount+1, dp[0]=0 0 coin, dp[i] means minimum number of coins we need to make up to dp[i](this amount)
        """
        dp = [float('inf')] * (amount+1)
        dp[0] = 0 # amount 0 no need coin
        for i in range(1, len(dp)):
            for c in coins:
                if i >=c:
                    dp[i] = min(dp[i], dp[i-c] + 1)
        return dp[-1] if dp[-1] != float('inf') else -1
