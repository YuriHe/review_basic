class Solution:
    """
    Question Minimum path sum 2d array
    1.create same size of 2d array
    2.handle basic case: fill out first column and first row
    """
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        m, n = len(grid), len(grid[0])
        dp = [[0 for j in range(n)] for i in range(m)]
        # base case
        dp[0][0] = grid[0][0]
        # fill in first row, come from left
        for j in range(1,n):
            dp[0][j] = grid[0][j] + dp[0][j-1]
        # fill in first column, come from top
        for i in range(1,m):
            dp[i][0] = grid[i][0] + dp[i-1][0]
        
        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                # cur minmax from top and left
                dp[i][j] = min(dp[i][j-1], dp[i-1][j]) + grid[i][j]
        return dp[-1][-1]