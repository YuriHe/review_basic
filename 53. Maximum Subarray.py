class Solution:
    """
    Question: use Kadane's algorithm -> O(n)
    negative value won't help sum larger, so cursum will reset if < 0 when iterate list
    """
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = nums[0]
        cursum = 0

        for n in nums:
            cursum = max(cursum, 0)
            cursum += n
            maxsum = max(cursum, maxsum)
        return maxsum
        