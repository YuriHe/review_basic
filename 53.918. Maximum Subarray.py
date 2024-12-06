class Solution:
    """
    53. Maximum Sum Subarray
    Question: use Kadane's algorithm -> O(n)
    negative value won't help sum larger, so cursum will reset if < 0 when iterate list
    """
    def maxSubArray(self, arr: List[int]) -> int:
        glo_max, cur_max = arr[0], 0
        for n in arr:
            # compare cur with previous sum
            cur_max = max(n, cur_max + n)
            glo_max = max(glo_max, cur_max)
        return glo_max

    
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
        