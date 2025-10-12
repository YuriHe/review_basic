class Solution:
    """
    QUESTION:Return T/F if find whole word in 2D grid
    SOLUTION1: memorization dfs 
    TIME: O(m*n*4^wl)
    """
    def exist(self, board: List[List[str]], word: str) -> bool:
        # set reuse variable
        m, n = len(board), len(board[0])
        # corner case
        if not board or m == 0 or n == 0: return False
        # declare 4-dir for search adjacent neighbors
        di = [[0,1],[0,-1],[1,0],[-1,0]]
        # declare visited 
        visited = [[False for _ in range(n)] for _ in range(m)]

        # declare bound helper
        def bound(i, j):
            return 0 <= i < m and 0 <= j < n

        # declare recursion helper
        def rec(ro, col, idx):
            # base positive case: done iteration
            if idx == len(word):
                return True
            # base negative case
            if not bound(ro, col) or visited[ro][col] or board[ro][col] != word[idx]:
                return False

            # still can serach next char
            visited[ro][col] = True

            # search next char from 4-dir
            for x, y in di:
                newX, newY = ro+x, col+y
                if rec(newX, newY, idx+1):
                    return True  # quick exit
            
            # finish all dfs start from [ro][col], no luck, unreset visited
            visited[ro][col] = False
            return False
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    # start doing dfs 
                    if rec(i, j, 0):
                        return True
        return False



