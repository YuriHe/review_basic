class Solution:
    """
    Question: rob one array
    """
    def rob(self, nums: List[int]) -> int:
        """
        SOLUTION1: bottom-up DP
        dp[i] means maximum accumulate value when rob at [i]
        """
        dp = [0] * len(nums)
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])

        for i in range(2, len(dp)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])

        return dp[-1]
        