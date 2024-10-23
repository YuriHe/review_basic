"""
    Question: steal maximum amount of $ but not steal two adjacent houses
    Topic: DP 1D
"""
def rob(self, nums: List[int]) -> int:
    # create dp array
    dp = [0] * len(nums)
    # base case
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return max(nums[0], nums[1])
    dp[0], dp[1] = nums[0], max(nums[0], nums[1])
    # dp func
    for i in range(2, len(dp)):
        # find max accumulated money for cur 
        dp[i] = max(dp[i-1], dp[i-2]+nums[i])
    return dp[-1]
