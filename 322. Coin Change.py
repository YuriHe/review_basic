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
        # define dp, assign default value amount+1 which impossible max value, size+1, skip 0
        dp = [amount+1] * (amount+1)
        dp[0] = 0 # no coin for 0 amount
        # dp[remain_coin] = dp[cur_amount-cur_coin]
        for i in range(1, len(dp)):
            # for current i amount, will have coins choices as beloow
            for c in coins:
                # cur coin is less than cur amount
                if i >= c:
                    # get minimum coins for cur amount, keep update dp[i] when traverse all coins 
                    dp[i] = min(dp[i], 1+dp[i-c])
        return dp[amount] if dp[amount] != amount+1 else -1
