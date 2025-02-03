class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        """
        1.Solution:two sliding window + two pointers to count length
        Idea: create one is increasing, another is decreasing
        T: O(n), S: O(1)
        """
        leftI, leftD, rightI,rightD = 0, 0, 1, 1
        max_len = 1

        # keep strictly increase
        while rightI < len(nums):
            if nums[rightI] <= nums[rightI-1]: # violated
                leftI = rightI
            max_len = max(max_len, rightI-leftI+1)
            rightI += 1
        # keep strictly decrease
        while rightD < len(nums):
            if nums[rightD] >= nums[rightD-1]: # violated
                leftD = rightD
            max_len = max(max_len, rightD-leftD+1)
            rightD += 1
        return max_len
        """
        2.Solution:Count increase/decrease + one pass (100% PASS)
        Idea: Iterate one loop, and update inc_len, dec_len
        T: O(n), S: O(1)
        """
        inc_len, dec_len, res = 1,1,1

        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                inc_len += 1
                dec_len = 1 # reset decreasing count
            elif nums[i] < nums[i-1]:
                dec_len += 1
                inc_len = 1 # reset increasing count
            else:# equal, so both reset
                dec_len = 1
                inc_len = 1
            res = max(res, dec_len, inc_len)
        return res