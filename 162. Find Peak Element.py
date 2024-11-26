"""
Question: Find peak局部最大值
1. return one of peak.
2. strictly greate than two neighbor
3. edge case: index 0(right less) and last 0(left less)

Binary search:
1. nums[mid] > nums[mid+1] -> peak on the left include mid
2. nums[mid] < nums[mid+1] -> peak on the right exclude mid
compare nums[mid] with nums[mid+1]
"""
def findPeakElement(self, nums: List[int]) -> int:
    if len(nums) <= 1: return 0 # no peak
    # SOLUTION1: O(n)
    for i in range(len(nums)):
        if i == 0 and nums[i+1] < nums[i]:
            return i
        elif i == len(nums) -1 and nums[i-1] < nums[i]:
            return i
        elif i-1>= 0 and i+1 < len(nums) and nums[i-1] < nums[i] and nums[i] > nums[i+1]:
            return i
    return 0

    # SOLUTION2: O(nlogn)
    l, r = 0, len(nums)-1
    while l < r:
        mid = (r + l) //2
        if nums[mid] > nums[mid+1]:
            r = mid
        else:
            l = mid +1
    return l

    