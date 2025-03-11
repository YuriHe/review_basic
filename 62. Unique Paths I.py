class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        SOLUTION1: bottom-top DP
        from base case, first row choice 1, first column choose 1, so [1][1]=2
        dp[i][j] is number of unique way to reach [i][j]
        result: dp[-1][-1] from left + top
        SPACE, TIME O(m*n)
        """
        dp = [[0 for _ in range(n)] for _ in range(m)]
        # give dp default value
        # first row have 1 choice
        dp[0][0] = 1
        for c in range(1, n):
            dp[0][c] = 1
        #first col have 1 choice
        for r in range(1, m):
            dp[r][0] = 1
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i][j-1] + dp[i-1][j]
        return dp[-1][-1]

        """
        SOLUTION2: bottom-top DP optimal
        from base case, first row choice 1, first column choose 1, so [1][1]=2
        dp[i][j] is number of unique way to reach [i][j]
        result: dp[-1][-1] from left + top
        TIME O(m*n),SPACE O(m)
        """
        dp = [0 for _ in range(n)] # define the number of way for each row
        # give dp default value
        # first row have 1 choice
        dp[0] = 1
        # first row
        for c in range(1, n):
            dp[c] = 1
        
        for r in range(1, m):
            for c in range(1, n):
                dp[c] = dp[c] + dp[c-1]
        return dp[-1]