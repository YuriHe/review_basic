class Solution:
    """
    Question: get number of flips to connect two islands
    BFS, visited + DFS find one island
    how do we know it is cur island or another island? -> find one island, dfs, flip them to *
    first find the island first and expand, if see * continue, see 0, count layer until reach 1
    """
    def shortestBridge(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        n = len(grid)
        m = len(grid[0])
        res = 0
        q = deque()
        dir = [[1,0], [-1, 0], [0, 1], [0, -1]]

        # helper - boundary
        def valid(i, j):
            return 0 <= i < n and 0 <= j < m

        # helper - dfs for first island
        def dfs(i, j):
            if grid[i][j] != 1:
                return
            grid[i][j] = 2
            q.append((i, j))

            for x, y in dir:
                nx = x + i
                ny = y + j
                if valid(nx, ny) and grid[nx][ny] == 1:
                    dfs(nx, ny)


        # Find first island using DFS and mark it
        found = False
        for i in range(n):
            if found:
                break
            for j in range(m):
                if grid[i][j] == 1:
                    # store cur island's coordinate to q and change to 2
                    dfs(i, j)
                    found = True
                    break
        
        while q:
            size = len(q)
            for _ in range(size):
                i, j = q.popleft()

                for x, y in dir:
                    nx = x + i
                    ny = y + j
                    if valid(nx, ny):
                        if grid[nx][ny] == 0: # expand into water 
                            q.append((nx, ny))
                            grid[nx][ny] = 2 # visited
                        elif grid[nx][ny] == 1: # found second island
                            # find shortest path
                            return res
            res += 1
        
        return -1




