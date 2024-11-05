import collections

class Solution:
    """
    Question: Valid existing sudoku with filled by num
    1.Check if duplicate each row/each column in whole sudoku use hashset
    2.Check if not digit
    3.Check if digit 1-9 only
    4.check subbox for 1,2,3
    How to differentiate subboxes -> can use r//3, c//3 -> 9box(0 1 2)
    """
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # create hashset {key: set} key is idx of row/col, set store num
        rows = defaultdict(set) 
        cols = defaultdict(set)
        # {(row_ith_box, col_ith-box): set()}
        box = defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                # check invalid 
                # duplicate in rows, columns, same subbox
                if board[i][j] in rows[i] or board[i][j] in cols[j] or board[i][j] in box[(i//3, j//3)]:
                    return False
                # update hashset
                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                box[(i//3, j//3)].add(board[i][j])
        return True


