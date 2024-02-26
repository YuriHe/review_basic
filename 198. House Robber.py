"""
    Question: steal maximum amount of $ but not steal two adjacent houses
    Topic: DP 1D
"""
def rob(self, nums: List[int]) -> int:
    # create dp list
    dp = [0] * len(nums)
    dp[0] = nums[0]
    if len(nums) == 1:
        return dp[0]
    dp[1] = max(nums[0], nums[1])

    for i in range(2, len(dp)):
        # compare cur+i-2 or i-1
        dp[i] = max(dp[i-1], dp[i-2] + nums[i])
    return dp[-1]
