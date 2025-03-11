class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        SOLUTION1: dfs
        TIME: O(M*N*4^L) L is word's length
        """
        m, n = len(board), len(board[0])
        di = [[0,1], [0, -1], [1, 0], [-1, 0]]
        visited = [[False for _ in range(n)] for _ in range(m)]

        def bound(i, j):
            return 0 <= i < m and 0 <= j < n

        def dfs(i, j, idx):
            if idx == len(word):
                return True
            if not bound(i, j) or visited[i][j] or board[i][j] != word[idx]:
                return False
            
            visited[i][j] = True

            for x, y in di:
                newX = i + x
                newY = j + y
                if dfs(newX, newY, idx+1):
                    return True
            visited[i][j] = False
            return False


        # iterate matrix
        for i in range(m):
            for j in range(n):
                if word[0] == board[i][j]:
                    # find first letter of word
                    if dfs(i, j, 0):
                        return True
        return False # not found the word