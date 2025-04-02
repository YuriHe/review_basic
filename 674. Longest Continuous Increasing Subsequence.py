class Solution:
    """
    Question: return length of longest increasing subarray
    """
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        """
        SOLUTION1: Array, compare neighbors
        TIME: O(n)
        SPACE: O(1)
        """
        if not nums: return 0
        # minimum length of increasing subarray
        res= 1
        cur = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                cur += 1
            else:
                res = max(res, cur)
                # reset cur length; start new subsequence from cur ele
                cur = 1
        # for final subsequence
        res = max(res, cur)
        return res
        """
        SOLUTION2: stack
        TIME SPACE O(n)
        """
        res = 0
        stack = []

        for i in range(len(nums)):
            if stack and nums[i] <= stack[-1]:
                while len(stack) > 0:
                    stack.pop()
            stack.append(nums[i])
            res = max(res, len(stack))
        
        return res