class Solution:
    """
    Question: number of unique path from top-left to bottom-right
    TOPIC: graph DP
    find number of ways -> DP
    DP top to down
    DP down to top
    """
    def uniquePaths(self, m: int, n: int) -> int:
        # SOLUTION1: DP BOTTOM-TOP
        # create 2D dp dp[0][0]
        dp = [[ 0 for j in range(n)] for i in range(m)]
        
        # base case go right and go down
        # iterate first column
        for i in range(m):
            dp[i][0] = 1
        # iterate first row
        for i in range(n):
            dp[0][i] = 1
        
        # dp function
        for i in range(1, m): # start 1 
            for j in range(1, n): # start 1
                # cur val from left and top
                dp[i][j] = dp[i][j-1] + dp[i-1][j]
        
        # return last one (bottom-right corner)
        return dp[m-1][n-1]

