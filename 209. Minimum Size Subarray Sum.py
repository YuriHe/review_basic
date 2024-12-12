class Solution:
    """
    Question: return minimum leng of consecutive sub array which sum >= target
    Cannot sort -> sliding window O(n)
    """
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # SOLUTIN1 Sliding window O(n)
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


    # SOLUTION2 binary O(nlogn) guess
        def valid_window(length):
            # check given length of window/subarray, find all valid subarray(sum>=target)
            prefixSum = 0
            for i in range(len(nums)):
                prefixSum += nums[i]
                if i >= length: # size larger than length expected, eg i=2, size is 3, but length=2
                    # remove left value
                    prefixSum -= nums[i-length]
                if prefixSum >= target:
                    return True
            return False

        # main part
        # low, high define length
        low, high = 1, len(nums)
        res = 0
        while low <= high:
            mid = (low + high) // 2
            if valid_window(mid):
                res = mid
                high = mid - 1
            else:
                low = mid + 1
        # If `res` is still 0, no subarray was found
        return res if res > 0 else 0



        
            
