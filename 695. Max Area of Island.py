class Solution:
    """
    Iterate 2d array find each island(area), compare them to find max_area
    """
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # use dfs 
        m, n = len(grid), len(grid[0])
        dir = [[0,1],[0,-1],[1,0],[-1,0]]

        def bound(i,j):
            return 0 <= i < m and 0 <= j < n and grid[i][j] == 1

        # use dfs to send data from bottom to top
        def dfs(i, j):
            # base case
            if not bound(i, j):
                return 0

            # update grid
            grid[i][j] = 0

            area = 1
            # explore whole one island
            for x, y in dir:
                newX, newY = x+i, y+j
                if bound(newX, newY):
                    area += dfs(newX, newY)
            return area

        # define max_area = 0
        max_area = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    # find one island, start dfs, update this area in the end 
                    max_area = max(max_area, dfs(i,j))

        return max_area