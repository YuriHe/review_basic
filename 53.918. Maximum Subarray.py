class Solution:
    """
    53. Maximum Sum Subarray
    Question: use Kadane's algorithm -> O(n)
    negative value won't help sum larger, so cursum will reset if < 0 when iterate list
    """
    # Largest sum of subarray
    # Kadane's algorithm -> O(n)
    def maxSubArray(self, arr: List[int]) -> int:
        # max_sum is maximum sum of any subarray found so far
        # max_end is maximum sum of the subarray ending at this cur index
        max_sum, max_end = float('-inf'), 0
        for i in range(len(arr)):
            # update the sum of subaray ending at this cur index
            max_end = max_end + arr[i]
            # update global maximum sum if cur subarray sum is larger
            max_sum = max(max_sum, max_end)
            # no positive, discard this subarray
            if max_end<0:max_end=0
        return max_sum

    
    """
    918. Maximum Sum Circular Subarray
    Question: handle max sum of circular subarray
    res = totol - minglosum or glo_max, check which larger
    edge case: all negative, -6--6=0 will be wrong, handle total != minglosum
    [0,-1,-2] -> 0
    """
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        glo_max, glo_min = nums[0], nums[0]
        cur_max, cur_min = 0,0
        total = 0

        for n in nums:
            cur_max = max(n, cur_max+n)
            cur_min = min(n, cur_min+n)
            glo_max = max(glo_max, cur_max)
            glo_min = min(glo_min, cur_min)
            total += n
        
        if glo_max < 0:
            return glo_max
        return max(total-glo_min, glo_max)
        