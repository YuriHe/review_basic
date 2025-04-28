class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        """
        SOLUTION2: find smallest a and b in ops
        TIME: O(k) k k times of operations
        """
        if not ops: return m*n
        a_min = min(op[0] for op in ops)
        b_min = min(op[1] for op in ops)
        return a_min*b_min
        """
        SOLUTION1: traverse 2d
        TIME: n^3
        """
        # create 2d array default value 0
        matrix = [[0 for j in range(n)] for i in range(m)]
        for op in ops:
            max_x, max_y = op[0], op[1]
            for i in range(max_x):
                for j in range(max_y):
                    matrix[i][j] += 1
        max_v = 0
        ctn = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] > max_v:
                    max_v = matrix[i][j]
                    ctn = 1
                elif matrix[i][j] == max_v:
                    ctn += 1
        return ctn
                