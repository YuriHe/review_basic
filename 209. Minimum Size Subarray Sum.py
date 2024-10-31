class Solution:
    """
    Question: return minimum leng of consecutive sub array which sum >= target
    Cannot sort -> sliding window O(n)
    """
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        size = len(nums) + 1 # find minimum length, set impossible v
        subsum = 0
        l, r = 0, 0 # dynamically re-size window
        while r < len(nums):
            subsum += nums[r]
            while l <= r and subsum >= target:
                # meet req
                size = min(size, r-l+1)
                # remove [left] from subsum
                subsum -= nums[l]
                # move on left pointer
                l += 1
            # move on right pointer
            r += 1
        return size if size != len(nums)+1 else 0




        
            
