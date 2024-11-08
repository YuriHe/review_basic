class Solution:
    """
    """
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # replace all 0 with x, except edge
        if not board or not board[0]: return
        
        # handle uncaptured subrrounded region starting from egde and dfs
        rows = len(board)
        cols = len(board[0])
        # first row & last row
        for j in range(cols):
            if board[0][j] == 'O':
                self.dfs(board, 0, j)
            if board[rows-1][j] == 'O':
                self.dfs(board, rows-1, j)
        # first column and last column
        for i in range(rows):
            if board[i][0] == 'O':
                self.dfs(board, i, 0)
            if board[i][cols-1] == 'O':
                self.dfs(board, i, cols-1)
        # revert region connecting to edge and change 0 to X subrrounded regions
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == '#':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'


    def dfs(self, board, i, j):
        # base case
        if not self.verify(board, i, j) or board[i][j] != 'O':
            return
        # mark 0 to # later revert back
        board[i][j] = '#'
        
        
        dir = [[0,1],[0,-1],[1,0], [-1, 0]]
        for x, y in dir:
            nx = x+i
            ny = y+j
            self.dfs(board, nx, ny)

        
    def verify(self, board, i, j):
        return i >= 0 and j >= 0 and i < len(board) and j < len(board[0])
