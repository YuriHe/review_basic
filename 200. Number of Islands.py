class Solution:
    """
    Question:return number of island(1's which surrounded by 0's)
    visited become 0 avoid recalculate
    modify grid value 1 to 0
    """
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        SOLUTION1: DFS
        """
        res = 0
        dire = [[1,0],[-1,0],[0,1],[0,-1]] # left, right, up, down

        def valid(i,j):
            return 0<=i<len(grid) and 0<=j<len(grid[0]) and grid[i][j]=="1"

        def dfs(i, j): # no return value
            # base case
            if not valid(i,j):
                return
            grid[i][j] = "0"

            # recursive case
            for x, y in dire:
                newX = x+i
                newY = y+j
                if valid(newX, newY): 
                    dfs(newX, newY)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1": # find edge of island
                    dfs(i, j)
                    res += 1
        return res