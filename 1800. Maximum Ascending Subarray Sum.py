class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        """
        1.Solution: Kadane's algorithm, strictly ascending, no need sliding window, no need prefix preprocess
        Time: O(n) Space: O(1)
        """
        res_sum, cur_sum = nums[0], nums[0]
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                cur_sum += nums[i]
            else:
                # not ascending, rest cur_sum
                cur_sum = nums[i]
            res_sum = max(res_sum, cur_sum)
        return res_sum
