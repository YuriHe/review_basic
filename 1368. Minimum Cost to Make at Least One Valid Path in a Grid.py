class Solution:
    """Question: minimum cost to get valid path from 0,0, to [m-1][n-1], 
    the cost means modifying the sign(based on current grid)
    Think dp with memorization, dp[i][j] is minimum cost to reach this cell keep updating
    dp[-1][-1] is end, see reversely 
    we can use dijkstra minheap
    T: m*n log(m*n)
    """
    
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[float('inf')] * n for _ in range(m)]
        # based on sign, 1:->, 2:<-, 3:down, 4: up
        dir = [[0,1], [0,-1], [1,0], [-1,0]]
        dp[0][0] = 0 # no cost at (0,0)
        minheap = []
        heapq.heappush(minheap, (0,0,0)) # (cost, x, y) # cost will be incremented

        def check(i,j):
            return 0<= i < m and 0 <= j < n

        while minheap:
            cost, x, y = heapq.heappop(minheap)
            if x == m-1 and y == n -1:
                return cost
            if cost > dp[x][y]: # that cost is not less than dp stored data continue
                continue
            # keep search
            for idx, (i, j) in enumerate(dir):
                newX, newY = x+i, y+j
                if check(newX, newY):
                    # check current cell x, y match direction of newX,newY
                    newcost = cost if grid[x][y] == idx+1 else cost+1
                    if newcost < dp[newX][newY]:
                        # update dp
                        dp[newX][newY] = newcost
                        # push to heap
                        heapq.heappush(minheap, (newcost, newX, newY))
        return -1


