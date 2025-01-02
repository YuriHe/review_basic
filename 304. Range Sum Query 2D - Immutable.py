class NumMatrix:
    """
    Question:rangeSum in 2D array
    Step:prehandle prefixsum += above and prefix every row(0,0 start point for all)
    Step:fetch subregion: [r2+1,c2+1]- abovesum-leftsum+topleftsum
    """
    def __init__(self, matrix: List[List[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])
        self.prefixsum = [[0 for j in range(COLS+1)] for i in range(ROWS+1)]
        # compute prefix
        for i in range(ROWS):
            # each row have prefix
            prefix =0
            for j in range(COLS):
                prefix += matrix[i][j]
                above = self.prefixsum[i][j+1]
                self.prefixsum[i+1][j+1] = prefix + above

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # cur region is row1, col1, row2, col2 all + 1
        above = self.prefixsum[row1][col2+1]
        left = self.prefixsum[row2+1][col1]
        topleft = self.prefixsum[row1][col1]
        return self.prefixsum[row2+1][col2+1] - above - left + topleft
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)