class Solution:
    """
    1004.
    Question: get longest subarray with 1 if flip at most k 0's
    Think available zero, no need to consider 1
    """
    def longestOnes(self, nums: List[int], k: int) -> int:
        res = 0
        l = 0
        zeroctn = 0

        for i in range(len(nums)): # right keep moving
            # count zero
            if nums[i] == 0:
                zeroctn += 1
            
            # check valid window
            if zeroctn <= k:
                res = max(res, i - l + 1)
            else:
                # invalid, move left
                if nums[l] == 0:
                    zeroctn -= 1
                l += 1
            
        return res


class Solution:
    """
    1493. Longest Subarray of 1's After Deleting One Element
    Question: Must Delete only one element 0 or extra1 and get longest subarray of 1's
    """
    def longestSubarray(self, nums: List[int]) -> int:
        l = 0
        zero = 0
        res = 0

        for r in range(len(nums)):
            if nums[r] == 0:
                zero += 1
            
            if zero <= 1:
                res = max(res, r-l) # must delete one 
            else:
                if nums[l] == 0:
                    zero -= 1
                l += 1
        return res
