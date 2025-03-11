class Solution:
    """
    Question: number of combination that make up to amount
    """
    def change(self, amount: int, coins: List[int]) -> int:
        """
        SOLUTION1: unbound Knapsack DP
        top-down 2D dp(DFS with memo) row: coin choice, column cell is amount
        unbounded:  infinite number of each kind of coin.
        dp[i] means the number of combination
        """
        memo = {} # (c, a): number of combination c is coin type, a is cur amount
        def dfs(c, a):
            if a == amount:
                return 1
            if a > amount:
                return 0
            if c == len(coins):
                return 0
            if (c, a) in memo:
                return memo[(c, a)]
            
            memo[(c, a)] = dfs(c, a+coins[c]) + dfs(c+1, a) # from left(choose cur coin) + from bottom(skip cur coin)
            return memo[(c,a)]

        return dfs(0, 0)

        """
        SOLUTION2: down top 1D dp
        dp[i] means number of ways to get i amount
        """
        dp = [0] * (amount+1)
        dp[0] = 1 # when combination, there is one way to make 0 amount: no coin is also one way
        for c in coins:
            # amount must choose >= c
            for a in range(c, amount+1):
                dp[a] += dp[a-c]
        return dp[-1]

