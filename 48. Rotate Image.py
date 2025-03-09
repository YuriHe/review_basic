# SOLUTION1
class Solution:
    """
    Question: know coordinate of 2d array
    HOW:rotate clock wise outer layer to inner layer
    STEP:
    1.first loop(l < r) :start four corner
    2.in loop, assgin left, right top, bottom(those are pos), while loop i < r-f, i is diff, i+pos point to the same layer
    3.store topleft, anticlowise replace slot start from right to left, bottom to top
    """
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        left, right = 0, len(matrix) - 1
        while left < right:  # if =, no need to rotate
            # define top/bottom
            top = left
            bottom = right
            # i + left/right/top/bottom pointing to next cell
            # matrix[top/bottom][left/right]
            for i in range(right-left): # right-left as diff, since first/last cell is filled
                # store top 
                temp = matrix[top][left+i]
                # left to top
                matrix[top][left+i] = matrix[bottom-i][left]
                # bottom to left
                matrix[bottom-i][left] = matrix[bottom][right-i]
                # right to bottom
                matrix[bottom][right-i] = matrix[top+i][right]
                # temp assign to topright
                matrix[top+i][right] = temp
            # done one layer

            # inner layer
            left += 1
            right -= 1
        

# SOLUTION2: BEST & SIMPLE
class Solution:
    """
    Question 90degree rotate matrix use clockwise direction
    Pattern: swap diagnal value(upper part) and reverse row by row 
    """
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(i, n): # start i+1, skip i=j pointing to same cell
                if i != j:
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        for row in matrix:
            row.reverse()
        

        
