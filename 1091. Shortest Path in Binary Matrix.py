from collections import deque

class Solution:
    def check(self, grid, i, j):
        return 0 <= i < len(grid) and 0 <= j< len(grid[0]) and grid[i][j]==0

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # check entrance and destination
        m, n = len(grid), len(grid[0])
        if grid[0][0] != 0 or grid[m-1][n-1] != 0: return -1
        dir = [[0,1],[1,0],[-1,0],[0,-1],[-1,-1],[1,1],[-1,1],[1,-1]]

        q = deque([])
        q.append((0,0))
        visit = set()
        visit.add((0,0))
        step = 1
        while q:
            size = len(q)
            for _ in range(size):
                curX, curY = q.popleft()
                if curX == m-1 and curY == n-1:
                    return step

                for x, y in dir:
                    if (curX+x, curY+y) not in visit and self.check(grid,curX+x, curY+y):
                        # push to q
                        q.append((curX+x, curY+y))
                        visit.add((curX+x, curY+y))
            step += 1
        return -1


