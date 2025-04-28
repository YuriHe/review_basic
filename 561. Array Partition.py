class Solution:
    """
    QUESTION: find maximum sum from the pair(len(nums)/2), If want to make sum largest, then values in pair
    should be closer, use sort
    """
    def arrayPairSum(self, nums: List[int]) -> int:
        """
        SOLUTION1: SORT and traverse half 
        TIME: Onlogn
        """
        nums.sort()
        res = 0
        for i in range(0, len(nums), 2):
            res += min(nums[i], nums[i+1])
        return res
        """
        SOLUTION2: counting sort
        """
        min_n = min(nums)
        max_n = max(nums)
        count = [0] * (max_n-min_n+1)
        for n in nums:
            count[n-min_n] += 1 # count diff
        sorted_n = []
        for i in range(len(count)):
            sorted_n.extend([i+min_n] * count[i]) # frequency of cur value occur
        return sum(sorted_n[::2])