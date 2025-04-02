class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix: return 0

        m, n = len(matrix), len(matrix[0])
        res = 0
        di = [[1,0],[-1,0],[0,1],[0, -1]]
        memo = [[-1 for _ in range(n)] for _ in range(m)]

        def bound(i, j):
            return 0<= i < m and 0 <= j < n
        
        def dfs(i, j):
            if memo[i][j] != -1:
                return memo[i][j]
            max_cur = 1 # current cell itself
            for x, y in di:
                newX = i+x
                newY = j+y
                if bound(newX, newY) and matrix[newX][newY] > matrix[i][j]:
                    max_cur = max(max_cur, 1+dfs(newX, newY))
            memo[i][j] = max_cur
            return max_cur


        # entrance
        for i in range(m):
            for j in range(n):
                res = max(res, dfs(i, j))
        return res
