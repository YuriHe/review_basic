"""
    Question: minimum length of subarray the sum >= target
    Topic: Sliding Window T:O(n) S:1
    Subarray is consecutive array 
    Solution1: use two pointer to control window
"""
def minSubArrayLen(self, target: int, nums: List[int]) -> int:
    size = len(nums)+1 # find minimum len, so set >maximum 
    i, j = 0,0
    subsum = 0
    while j < len(nums):
        # add cur to subsum & update subsum 
        subsum += nums[j]
        # handle left and shrink subsum
        while i <= j and subsum >= target:
            size = min(size, j-i+1)
            subsum -= nums[i]
            i += 1
        j += 1
    return 0 if size == len(nums)+1 else size