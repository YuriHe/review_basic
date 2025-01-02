class Solution:
    """
Question:maximum length of subarray with 0's and 1's-> sum is 0
Topic:hashmap store{sum:index} valid i
    """
    def findMaxLength(self, nums: List[int]) -> int:
        # modify all 0 to -1, and make sum = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i] = -1
        res = 0
        sumMap = {}
        sumMap[0] = -1 # dont miss first ele
        prefix = 0
        for i in range(len(nums)):
            prefix += nums[i]
            if prefix in sumMap:
                res = max(res, i - sumMap[prefix])
            else:
                sumMap[prefix] = i
        return res
