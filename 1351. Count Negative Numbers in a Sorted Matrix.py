"""
    Question: search negative in descendingly sorted matrix 
    Topic: Two pointer T:O(n+m) S:O(1)
    Starting last row, search row by row if not found, colume by colume if found search more
    [[4,2,1]
     [0,-2,-4]]
"""
def countNegatives(self, grid: List[List[int]]) -> int:
    row = len(grid)
    col = len(grid[0])
    r = row - 1 # start from last row
    c = 0
    res = 0
    while r >=0 and c < col:
        if grid[r][c] < 0: 
            res += col-c # this row start[r][c] are negative len-index=amount
            # go up to search more negative in new row
            r -= 1
        else:
            # now positive, go right to see if any negative
            c += 1
    return res