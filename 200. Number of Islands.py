class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def valid(i, j):
            return 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == "1"

        def dfs(i, j):
            dir = [[1,0], [-1, 0], [0, 1], [0, -1]]
            # base case
            if not valid(i, j):
                return
            # visited
            grid[i][j] = "0"
            for x, y in dir:
                newX = i + x
                newY = j + y
                dfs(newX, newY)

        # dfs
        m,n = len(grid),len(grid[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    dfs(i, j) # work inside single one island
                    res += 1
        return res