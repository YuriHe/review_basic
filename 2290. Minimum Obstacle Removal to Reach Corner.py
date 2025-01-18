class Solution:
    """
    Question: minimum remove from start to end
    1solution backtrack find all solutions, and pick minium removal: Time: 4 ^ m*n
    """
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        # 1 Solution: backtrack TLE
        m, n = len(grid), len(grid[0])
        dir = [[0,1],[1,0],[-1,0],[0,-1]]
        visit = [[False] * n for _ in range(m)]
        res = float('inf')

        def dfs(x, y, removed):
            nonlocal res
            # satified
            if x == m-1 and y == n-1:
                res = min(res, removed)
                return
            # update visited
            visit[x][y] = True
            # search
            for i, j in dir:
                newX = x+i
                newY = y+j
                if check(newX, newY) and not visit[newX][newY]:
                    dfs(newX, newY, removed+grid[newX][newY])
            # unset 
            visit[x][y] = False

        dfs(0,0,0)
        return res

        # 2 Solution Dijkstra alogirhtm minheap(pq)
        # use minheap: T(m*n)*log(m*n). S:(m*n)
        m, n = len(grid), len(grid[0])
        dir = [[0,1],[1,0],[-1,0],[0,-1]]
        q = []
        heapq.heappush(q, (0,0,0)) # (removed, x, y). removed must first since minheap use it to sort
        visit = [[False] * n for _ in range(m)]

        def check(i, j):
            return 0 <= i < m and 0 <= j< n

        while q:
            removed, x, y = heapq.heappop(q)
            if x == m-1 and y == n-1:
                return removed # remove right away since it is minimum removal
            if visit[x][y]:
                continue
            # update visited
            visit[x][y] = True

            for i, j in dir:
                newX,newY = x+i, y+j
                if check(newX, newY) and not visit[newX][newY]:
                    if grid[newX][newY] == 1:
                        heapq.heappush(q, (removed+1, newX, newY))
                    else:
                        heapq.heappush(q, (removed, newX, newY))
        return -1

