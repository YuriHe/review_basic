class Solution:
    """
    63. Unique Paths II
    """
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        """
        SOLUTION1: bottom-top DP
        TIME, SPACE O(m*n)
        """
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        # start is obstacle
        if obstacleGrid[0][0] == 1: return 0

        # create dp size m+1, n+1
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = 1
        # give dp default value
        # first row have 1 choice
        for c in range(1,n):
            if obstacleGrid[0][c] == 1:
                # obstacle,no path
                dp[0][c] = 0
            else:
                # carry over vale from left
                dp[0][c] = dp[0][c-1]

        #first col have 1 choice
        for r in range(1,m):
            if obstacleGrid[r][0] == 1:
                dp[r][0] = 0
            else:
                dp[r][0] = dp[r-1][0]
        
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i][j-1] + dp[i-1][j] # from left and above
        return dp[-1][-1]
        """
        SOLUTION2: Optimize bottom-top DP
        no need 2D dp -> 1dp [i] get number of unique for this col
        because (i,j) depend dp[j-1] left cell, dp[j] above cell
        SPACE: O(n)
        """
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1: return 0
        dp = [0 for _ in range(n)]
        dp[0] = 1
        # first row
        for c in range(1, n):
            if obstacleGrid[0][c] == 1:
                dp[c] = 0
            else:
                dp[c] = dp[c-1]
        # fill rest of grid
        for r in range(1, m):
            # handle first column
            if obstacleGrid[r][0] == 1:
                dp[0] = 0
            # handle rest of columns
            for c in range(1, n):
                if obstacleGrid[r][c] == 1:
                    dp[c] = 0
                else:
                    dp[c] = dp[c] + dp[c-1]
        return dp[-1]