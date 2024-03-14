class Solution:
    """
    Question: search full word from 4 directions
    TOPIC: DFS, 2D
    T/S: O(n^2)
    """
    def exist(self, board: List[List[str]], word: str) -> bool:
        if word is None or len(word) == 0: return False
        visit =[[False for j in range(len(board[0]))]for i in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]: 
                    # find first char of word, do 4 directions search
                    if self.dfs(board, i, j, word, 0, visit):
                        return True
        return False
    
    def isInBoard(self, board, i, j):
        return i >=0 and i < len(board) and j >= 0 and j < len(board[0])

    def dfs(self, board, x, y, word, word_index, visit):
        # base case
        if word_index == len(word)-1:
            return board[x][y] == word[word_index]

        # only find char then do dfs
        if word[word_index] == board[x][y]:
            visit[x][y] = True
            dir =[[0,1],[1,0], [0,-1], [-1,0]]
            for i, j in dir:
                wx = x + i
                wy = y + j
                if self.isInBoard(board, wx, wy) and not visit[wx][wy] and self.dfs(board, wx, wy, word, word_index+1, visit):
                    # mean find full word
                    return True
            # otherwise, stop search 4 directions
            #not found, reset 
            visit[x][y] = False
        
        # Not found
        return False
        