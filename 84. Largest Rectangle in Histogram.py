class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Nlogn 1SOLUTION: divide and conquer
        def divide(start, end):
            if start > end: return 0
            # assume minheightindex is start for this segment
            minIndex = start
            for i in range(start, end+1, 1):
                if heights[i] < heights[minIndex]:
                    minIndex = i
            curArea = heights[minIndex] * (end-start+1)
            # recursive
            left = divide(start, minIndex-1) # end included
            right = divide(minIndex+1, end)
            return max(curArea,left, right)

        return divide(0, len(heights)-1)

        # 2SOLUTION: monotonically increasing stack
        # Stack to store indices,maintain increasing stack
        stack = []
        res = 0
        # add 0 at the end to flush stack(0 is min)
        heights.append(0)
        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                top = stack.pop()
                higher = heights[top]
                # Width is from the previous index in the stack to the current index
                width = i if not stack else i - stack[-1]- 1 # stack[-1] second top
                res = max(res, higher * width)
            stack.append(i)
        return res