class Solution:
    """
    Question: min & max replaceable range 
    No about index, only max min range!
    2,    3,   4,   5,   6,   7.   k =2
    i+0, i+1, i+2, i+3, i+4. i+5
    eg.min=2, max=7
    max=7:replaceable range[5,9]
    min=2:replaceable range[0,4]
    non-overlap -> cannot replace 
    overlap -> can replace
    min+k: 2+2=4
    max-k: 7-2=5 (no overlap)
    max-min=7-2 ?<= 2*k (No, time to move left of window)
    if finally: 
    replace nums[i] with number from [nums[i]-k, nums[i]+k]
    number is monotonic: range n+k....
    1.Sort
    2.valid window is replaceable range also is longest subsequence
    """
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        i = 0
        res = 0

        for j in range(len(nums)):
            # move left of window
            while nums[j] - nums[i] > 2* k:
                i += 1
            res = max(res, j-i+1)
        return res
