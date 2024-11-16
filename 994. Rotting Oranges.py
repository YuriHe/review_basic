class Solution:
    """
    Question: graph 2D
    if still 2, return -1; otherwise minute(include 0)
    bfs since in the grid, many oranges will rotten at the same time
    """
    def check(self, grid, i, j):
        return i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0])

    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]: return 0
        fresh = 0
        minute = 0
        dir = [[1,0], [-1,0], [0,1], [0,-1]]
        q = deque([]) # store tuple

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2: # found rotted at 0 minute
                    q.append((i, j))
        if fresh == 0:
            return minute # no rotted at begin

        while len(q) > 0 and fresh > 0: # OPTIMIZE, check fresh, so no need minute-1 for last rotten
            minute += 1
            size = len(q)
            for _ in range(size):  # OPTIMIZE,NOT USE while size > 0 then size --
                first = q.popleft()
                
                for x, y in dir:
                    nx = x + first[0]
                    ny = y + first[1]
                    if self.check(grid, nx, ny) and grid[nx][ny] == 1:
                        # push to q
                        q.append((nx, ny))
                        fresh -= 1
                        grid[nx][ny] = 2

        return -1 if fresh != 0 else minute


        
            