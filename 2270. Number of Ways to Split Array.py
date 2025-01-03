class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        # 1 SOLUTION prefixsum list
        res = 0
        # prefix sum prework
        if not nums: return 0
        prefixsum = [0] * len(nums)
        prefixsum[0] = nums[0]
        for i in range(1, len(nums)):
            prefixsum[i] = prefixsum[i-1] + nums[i]
        idx = 0
        while idx < len(nums)-1: # at least one on the right of i
            latter = prefixsum[-1] - prefixsum[idx]
            
            if prefixsum[idx] >= latter:
                res += 1
            idx += 1
        return res

        # 2SOLUTION sum variable
        if not nums: return 0
        res = 0
        total = sum(nums)
        prefix = 0
        for i in range(len(nums)-1):
            prefix += nums[i]
            if prefix >= total - prefix:
                res += 1
        return res