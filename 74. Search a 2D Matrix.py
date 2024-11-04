class Solution:
    """
    Question: sorted 2D array, use binary search, handle coordinates
    rows =3, columns = 4
    low = 0, high = m*n-1       eg.0, 3*4-1=11
    mid = (low+high) // 2       eg.5
    midrow = mid // columns     eg.1
    midcol = mid % columns.     eg.1
    """
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]: return False
        rows = len(matrix)
        cols = len(matrix[0])

        i, j = 0, rows*cols-1

        while i <= j:
            mid = (i+j) // 2
            mid_row = mid // cols
            mid_col = mid % cols

            if matrix[mid_row][mid_col] == target:
                return True
            elif matrix[mid_row][mid_col] > target:
                j = mid -1
            else:
                i = mid + 1
        return False