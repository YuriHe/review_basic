class Solution:
    """
    Question: return minimum number of operation to make sum of modified array divisible by k
    """
    def minOperations(self, nums: List[int], k: int) -> int:
        # SOLUTION1: loop
        # res,idx,l = 0,0, len(nums)

        # while True:
        #     if sum(nums) % k == 0:
        #         return res
        #     nums[idx % l] = nums[idx % l] - 1
        #     idx += 1
        #     res += 1
        
        # SOLUTION2: math
        # each operation total-1, so at least sum%k times
        return sum(nums) % k
