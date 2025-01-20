class Solution:
    """
    Question:return smallest index from arr. 
    Go through arr and continue painting according value in mat until one whole row oor column is completely painted
    Time: max(m, n) ^2
    Space: max(m, n)
    """
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        # rowArray Count, check if val = n then return index from arr
        rowArr = [0] * m
        colArr = [0] * n
        # prehandle position of mat
        valIndex = collections.defaultdict(int)
        for i in range(m):
            for j in range(n):
                valIndex[mat[i][j]] = (i, j)

        for i in range(len(arr)):
            # find i, j from dict
            pi,pj = valIndex[arr[i]]
            rowArr[pi] += 1
            colArr[pj] += 1
            if rowArr[pi] == n:
                return i
            if colArr[pj] == m:
                return i
        return -1
