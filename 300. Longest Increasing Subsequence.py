"""
    Question: longest increaseing subsequence(not continuous) of number
    Bottom-up DP
    two loops for find increasing subsequence at certain range
    return max(dp), this time, last value of dp is not anwser
"""
# SOLUTION1: O(n^2)
def lengthOfLIS(self, nums: List[int]) -> int:
    # define dp array
    dp = [1] * len(nums)

    for i in range(1, len(dp)): # i is right pointer
    # for i as right pointer of sequence, dp[i] will have multiple res, to pick max
        for j in range(i):
            if nums[i] > nums[j]:
                # 2,5,3,7 -> 2,3,7 choose max
                dp[i] = max(dp[i], dp[j]+1)
    return max(dp)
