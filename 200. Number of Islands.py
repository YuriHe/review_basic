class Solution:
    """
    Question: check number of islands, if four edges are 0
    Topic: DFS
    """
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        # iterate 2d array
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    res += 1
                    #find part of island
                    # spread out 
                    self.dfs(grid, i, j)
        return res

    def dfs(self, grid, i, j):
        # base case
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != "1":
            return
        # update current grid[i][j] as visited
        grid[i][j] = "2"
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)
    
        