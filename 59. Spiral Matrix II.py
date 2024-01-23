"""
    Question: n*n metrics in spiral order 1 to n^2, return 2D array
    Topic: 2D array pos
    Use left,right,top,bottom 4pointers and other pointer for assign val
"""
def generateMatrix(self, n: int) -> List[List[int]]:
    if n == 0: return [[]]
    # create 2D array
    arr =[[0 for j in range(n)] for i in range(n)]
    left, right, top, bottom = 0, n, 0, n
    start = 1
    while left < right and top < bottom:
        # assign first row
        for i in range(left, right):
            arr[top][i] = start
            start += 1
        top += 1
        # assign last column
        for i in range(top, bottom):
            arr[i][right-1] = start
            start += 1
        right -= 1
        # assign last row right to left
        for i in range(right-1, left-1, -1):
            arr[bottom-1][i] = start
            start += 1
        bottom -= 1
        # assign first colume
        for i in range(bottom-1, top-1, -1):
            arr[i][left] = start
            start += 1
        left += 1

    return arr
