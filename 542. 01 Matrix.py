class Solution:
    """
    Return the modified grid. skip 0, when see 1, then do bfs, find nearest 0 count distance -> Dijkstra algorithm or bfs 
    """
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        dir = [[0,1],[1,0],[-1,0],[0,-1]]

        def check(i, j):
            return 0 <= i < m and 0 <= j< n and mat[i][j] == -1

        q = deque()
        # find all zero and push their i, j to queue
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append((i, j))
                else:
                    mat[i][j] = -1 # no process(like visit)

        # handle q, distance store mat2 
        while q:
            x,y = q.popleft()

            for i,j in dir:
                newX, newY = x+i, y+j
                if check(newX, newY):
                    # which mean within boundary and not process
                    mat[newX][newY] = mat[x][y] + 1
                    q.append((newX, newY)) # push newx,y to queue, so distance from 0 will update
        return mat


