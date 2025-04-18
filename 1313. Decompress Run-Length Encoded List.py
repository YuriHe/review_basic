class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        """
        SOLUTION1: traverse list
        """
        res = []
        for i in range(len(nums)):
            if 2*i+1 < len(nums) and 2*i < len(nums)-1:
                freq = nums[2*i]
                val = nums[2*i+1]
                tmp = [val] * freq
                res.extend(tmp)
        return res
        """
        SOLUTION2: optimize enumeration, every 2times
        """
        res = []
        for i in range(0, len(nums), 2):
            freq = nums[i]
            val = nums[i+1]
            res.extend([val]*freq)
        return res
