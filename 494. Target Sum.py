class Solution:
    """
    Question: Do +/- operations to meet target
    Topic: total ways/combination/recursion/DP/top-down
    # Solution1: Memorization DP, top-down recursion
    """
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        index = len(nums) - 1
        curr_sum = 0
        self.memo = {}
        return self.dp(nums, index, target, curr_sum)
    
    def dp(self, nums, index, target, curr_sum):
        # avoid overhead
        if (index, curr_sum) in self.memo:
            return self.memo[(index, curr_sum)]

        # base case
        if index < 0 and curr_sum == target:
            # find one way for target sum
            return 1
        if index < 0:
            # not found
            return 0

        # decisions
        positive = self.dp(nums, index-1, target, curr_sum+nums[index])
        negative = self.dp(nums, index-1, target, curr_sum-nums[index])
        
        # store to memorization dict 
        # key is tuple(index, cursum)
        self.memo[(index, curr_sum)] = positive+negative
        return self.memo[(index, curr_sum)]
