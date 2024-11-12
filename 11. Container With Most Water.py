class Solution:
    """
    Question: find maximum x * y area, two loops two pointers,
    """
    def maxArea(self, height: List[int]) -> int:
        # SOLUTION1 TLE
        area = 0
        for i in range(len(height)):
            for j in range(1, len(height)):
                n = min(height[i], height[j]) * (j-i)
                area = max(area, n)
        return area

        # SOLUTION2 TWO POINTER
        res = 0
        i, j = 0, len(height)-1
        while i < j:
            res = max(res, (j-i) * min(height[i], height[j]))

            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return res