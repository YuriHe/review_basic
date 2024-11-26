class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        73. Set Matrix Zeroes
        Do not return anything, modify matrix in-place instead.
        flip cur 0 only
        dont change to # which will affect original 0
        """
        flipR = set()
        flipL = set()

        n = len(matrix)
        m = len(matrix[0])
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    flipR.add(i)
                    flipL.add(j)
        
        for r in flipR:
            for j in range(m):
                matrix[r][j] = 0
        for j in flipL:
            for i in range(n):
                matrix[i][j] = 0

class Solution:
    """
    289. Game of Life
    live or die at the same time -> don't modify one by one, use set/map store status
    cur 1 -> 0 when adj <2 1's; adj > 3 1's 
    cur 0 -> 1 when adj ==3 1's.
    """
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        m = len(board[0])
        dir = [[1,0], [-1, 0], [1,1], [-1,-1], [0,1], [0, -1],[1,-1], [-1, 1]]

        def valid(i, j):
            return i >= 0 and j >= 0 and i < n and j < m

        # store (i, j)tuple to the set
        live = set() # change 0 to 1
        die = set() # change 1 to 0

        for i in range(n):
            for j in range(m):
                if board[i][j] == 1:
                    num1 = 0
                    for x, y in dir:
                        nx,ny = x + i, y + j
                        if valid(nx, ny):
                            if board[nx][ny] == 1:
                                num1 += 1
                    if num1 > 3 or num1 < 2:
                        die.add((i, j))
                else: # it is 0
                    num1 = 0
                    for x, y in dir:
                        nx,ny = x + i, y + j
                        if valid(nx, ny):
                            if board[nx][ny] == 1:
                                num1 += 1
                    if num1 == 3:
                        live.add((i, j))
        
        for i, j in live:
            board[i][j] = 1
        for i, j in die:
            board[i][j] = 0

