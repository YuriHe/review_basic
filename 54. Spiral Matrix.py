class Solution:
    """
    Question: spiral matrix
    handle idx & boundary
    """
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        n, m = len(matrix), len(matrix[0])
        r1, c1 = 0,0
        r2, c2 = n-1, m-1
        res = []

        while r1<=r2 and c1<=c2:
            # first row
            for c in range(c1, c2+1):
                res.append(matrix[r1][c])

            # last column
            for r in range(r1+1, r2+1):
                res.append(matrix[r][c2])

            # last row
            if r1 < r2: # if more than one row
                for c in range(c2-1, c1-1, -1):
                    res.append(matrix[r2][c])

            # first column
            if c1 < c2: # if more than one col
                for r in range(r2-1, r1, -1):
                    res.append(matrix[r][c1])

            #handle second round
            r1 = r1+1
            r2 = r2-1
            c1 = c1+1
            c2 = c2-1
    
        return res

