class Solution:
    """
    QUESTION: find maximum value of (n[i]-n[j]) * n[k] under i<j<k
    """
    def maximumTripletValue(self, nums: List[int]) -> int:
        """
        SOLUTION1: Brute force, Iterate unsorted list, update res
        TIME: O(n^3), SPACE: O(1)
        SOLUTION2: Greedy
        HOW: Let k, j position fixed, find max value of equation.
        TIME: O(n^2), SPACE: O(1)
        """
        if len(nums) < 3: return 0
        res = 0
        for k in range(2, len(nums), 1): # k is last index of ele
            first = nums[0]
            for j in range(1, k, 1): # j is second index of ele
                res = max(res, (first - nums[j]) * nums[k])
                first = max(first, nums[j]) # update max value of first
        return res
            
        