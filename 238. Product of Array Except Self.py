class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        1.Solution: Prefix from left to right and right to left
        Time: O(n), Space: O(n)
        """
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)
        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i-1]
        
        for i in range(len(nums)-2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]
        
        res = [] 
        for i in range(len(prefix)):
            res.append(prefix[i] * suffix[i])
        return res
        """
        2.Solution: Prefix from without array memory
        Time: O(n), Space: O(1)
        """
        prefix,suffix = 1, 1
        res = [1] * len(nums) 
        for i in range(1, len(nums)):
            prefix = prefix * nums[i-1]
            res[i] = prefix
        
        for i in range(len(nums)-2, -1, -1):
            suffix = suffix * nums[i+1]
            res[i] = res[i+1] * suffix
        
        return res