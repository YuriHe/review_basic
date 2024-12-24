class Solution:
    """
    Return all solutions with N
    """
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        # create original grid
        grid = [["." for _ in range(n)] for _ in range(n)]
        # below is Queen already in row, column, left Diagonal, right Diagonal
        rowS = set()
        colS = set()
        leftD = set()
        rightD = set()

        def rec(row):
            # base case
            if row==n:
                # finish whole grid all rows
                res.append(["".join(grid[i]) for i in range(n)])
                # res.append(["".join(r) for r in grid])
                return
            # iterate cur row's all columns
            for j in range(n):
                # check if already visit or marked DONT changee
                if row in rowS or j in colS or row-j in leftD or row+j in rightD:
                    continue # search next column
                # validate and update status
                grid[row][j] = "Q"
                rowS.add(row)
                colS.add(j)
                leftD.add(row-j)
                rightD.add(row+j)
                # recusion call for next row for cur column
                rec(row+1)
                # backtrack
                grid[row][j] = "."
                rowS.remove(row)
                colS.remove(j)
                leftD.remove(row-j)
                rightD.remove(row+j)
        rec(0)
        return res
