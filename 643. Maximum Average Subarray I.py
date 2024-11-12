class Solution:
    """
    Question: max sum subarray with size 
    sliding window 
    """
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxtotal = 0
        # get sum with k size
        for i in range(k):
            maxtotal += nums[i]

        left, right = 0, k
        winsum = maxtotal
        while right < len(nums):
            winsum += nums[right]
            winsum -= nums[left]
            maxtotal = max(maxtotal, winsum)
            
            left += 1
            right += 1
        
        return maxtotal / k
