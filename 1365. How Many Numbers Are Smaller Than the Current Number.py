class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        """
        SOLUTION1: count occurence + prefix sum
        TIME: O(n)
        """
        # create count array max+1 as length, to count frequency of this number
        max_num = max(nums)
        count = [0] * (max_num+1)
        for n in nums:
            count[n] += 1
        # create prefix_ctnsum array max+1 as length to count how many number less than current 
        prefix_ctn_sum = [0] * (max_num+1)
        for i in range(1, len(prefix_ctn_sum)):
            prefix_ctn_sum[i] = prefix_ctn_sum[i-1] + count[i-1]
        res = []
        for n in nums:
            res.append(prefix_ctn_sum[n])
        return res
