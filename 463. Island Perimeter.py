class Solution:
    """
    Define count current sides: if 0 , bound 
    use dfs 
    """
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        """
        1SOLUTION:dfs
        """
        visit = set()
        dir = [[1,0], [-1, 0], [0,1], [0, -1]]
        def check(i, j):
            return 0 <= i < len(grid) and 0 <= j < len(grid[0])
        
        def dfs(i, j):
            # base case
            if (i, j) in visit:
                return 0
            if not check(i, j):
                return 1
            if grid[i][j] == 0:
                return 1

            visit.add((i,j))
            return dfs(i+1, j)+ dfs(i-1, j) + dfs(i, j-1) + dfs(i, j+1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    # find island 
                    return dfs(i, j)
        return -1
        """
        2SOLUTION: observe +4 first, later if check top and left which are visited -=1
        """
        if not grid or not grid[0]: return 0
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    res += 4
                    if i-1>= 0 and grid[i-1][j] == 1:
                        res -= 2 # sides from top and cur
                    if j-1>= 0 and grid[i][j-1] == 1:
                        res -= 2 # sides from left and cur
        return res


