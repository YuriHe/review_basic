class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1": # that is part of island, start dfs
                    self.dfs(grid, i, j)
                    res += 1
        return res

    def dfs(self, grid, i, j) -> None:
        if grid[i][j] != "1":
            return
        # visited
        grid[i][j] = "0"

        dir = [[1,0], [-1, 0], [0,1], [0, -1]]
        for x, y in dir:
            nx = i + x
            ny = j + y
            # explore all 4 direction and change all 1 to 0
            if self.check_bound(grid, nx, ny):
                self.dfs(grid, nx, ny)

        
    def check_bound(self, grid, i, j):
        if i >= 0 and j >= 0 and i < len(grid) and j < len(grid[0]):
            return True
        return False