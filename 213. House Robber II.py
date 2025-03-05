class Solution:
    """
    Question:rob in a circle
    cannot rob first and last house
    circle turns to subproblem
    Rob houses from the first house to the second-to-last house (i.e., exclude the last house).
    Rob houses from the second house to the last house (i.e., exclude the first house).
    Run _dp() twice, return max result
    """
    def rob(self, nums: List[int]) -> int:
        """
        SOLUTION1: bottom up DP
        """
        def _dp(ns):
            n = len(ns)
            if n == 0:
                return 0
            if n == 1:
                return ns[0]

            dp = [0] * n
            dp[0], dp[1] = ns[0], max(ns[0],ns[1])

            for i in range(2, len(dp)):
                dp[i] = max(dp[i-1], dp[i-2] + ns[i])
            return dp[-1]

        if not nums: return 0
        elif len(nums)==1: return nums[0]
        else:
            return max(_dp(nums[:-1]), _dp(nums[1:]))
