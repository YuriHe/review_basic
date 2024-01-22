"""
    Question:return sorted array of squares
    Solution1: sort O(n) + O(nlogn)
    Solution2: Three pointers, mostleft and mostright is largest and also replace in list
    Issue: [-5,-3,-2,-1]-> [25,9,4,1] ->[1,9,4,25]->compare 1 and 4, so must have new arr to track largest, not just easily compare two in existing arr
    """
def sortedSquares(self, nums: List[int]) -> List[int]:  
    # Solution1
    # return sorted(n**2 for n in nums)
    # Solution2 
    # create new array instead of change existing nums
    res = [0] * len(nums)
    k = len(res) - 1
    i = 0
    j = len(nums)-1
    while i <= j:
        if nums[i] * nums[i] > nums[j] * nums[j]:
            res[k] = nums[i] * nums[i]
            i += 1
            k -= 1
        else:
            res[k] = nums[j] * nums[j]
            j -= 1
            k -= 1
    return res
        