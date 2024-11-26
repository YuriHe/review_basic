class Solution:
    """
    Question: 62. Unique Path
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

    def uniquePaths(self, m: int, n: int) -> int:
        # SOLUTION2: DP TOP-BOTTOM WITH memo
        memo = {}
        @cache
        def dfs(i, j):
            if (i, j) in memo: return memo[(i,j)]
            if i >= m or j >= n: return 0
            if i == m-1 and j == n-1: return 1 # that path works from topleft to bottom right

            memo[(i,j)] = dfs(i, j+1) + dfs(i+1, j)
            return memo[(i,j)]

        return dfs(0,0)


"""
    63. Unique Paths II have obstacles
    get the number of unique paths, -> DP
    Topto bottom with memorization
    if i >= n or j >= m, or [i][j] == 1 then the number of path is 0
    if i == n-1 and j == m-1 then reach path + 1
"""
def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
    if not obstacleGrid: return 0
    memo = {} # (i,j): number of path
    n, m = len(obstacleGrid), len(obstacleGrid[0])

    @cache
    def dfs(i, j):
        if (i, j) in memo: return memo[(i,j)]
        # base case
        if i >= n or j >= m or obstacleGrid[i][j] == 1: return 0
        if i == n - 1 and j == m-1: return 1
        memo[(i,j)] = dfs(i, j+1) + dfs(i+1, j)
        return memo[(i,j)]

    return dfs(0,0)