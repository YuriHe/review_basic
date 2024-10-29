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
        left, right = 0, len(height)-1
        while left < right:
            # update
            border = min(height[left], height[right])
            res = max(res, border * (right-left))
            # move 
            if height[left] > height[right]:
                right -= 1
            else: # no need to ==, move both will reduce area, pick left or right
                left += 1 

        return res
                