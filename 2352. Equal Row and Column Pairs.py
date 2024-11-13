class Solution:
    """
    Question: find the number of pairs that row array = column array
    ! duplicate rows/columns should be considered as well
    """
    def equalPairs(self, grid: List[List[int]]) -> int:
        temp = defaultdict(int)
        res = 0

        # store row by row
        for r in range(len(grid)):
            inner = [] # store each row
            for c in range(len(grid[0])):
                inner.append(grid[r][c])
            temp[tuple(inner)] += 1

        # check column by column
        for c in range(len(grid[0])):
            inner2 = []
            for r in range(len(grid)):
                inner2.append(grid[r][c])
            if tuple(inner2) in temp:
                res += temp[tuple(inner2)]
        
        return res


