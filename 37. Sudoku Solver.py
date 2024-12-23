class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        Space: recursive: O(n), hashset: 9*9=81 O(1) => total is O(n)
        Time: O(9^n) for backtracking, 9*9*....

        """
        rowS = defaultdict(set) 
        colS = defaultdict(set)
        # {(row_ith_box, col_ith-box): set()}
        box = defaultdict(set)
        empty = []
        
        # fill existing board
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != '.':
                    rowS[i].add(board[i][j])
                    colS[j].add(board[i][j])
                    box[(i//3, j//3)].add(board[i][j])
                else:
                    empty.append((i, j))
        
        # recursively empty list and fill out empty cell
        def rec(index):
            if index == len(empty):
                return True

            i, j = empty[index]
            for v in range(1, 10):
                char = str(v)
                if char in rowS[i] or char in colS[j] or char in box[(i//3, j//3)]:
                    continue
                # valid char and updates all hashset,modify board
                rowS[i].add(char)
                colS[j].add(char)
                box[(i//3, j//3)].add(char)
                board[i][j] = char

                # search next one 
                if rec(index+1):
                    return True
                
                # backtrack reset
                rowS[i].remove(char)
                colS[j].remove(char)
                box[(i//3, j//3)].remove(char)
                board[i][j] = "."
            
        rec(0)
        