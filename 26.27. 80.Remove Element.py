"""
    26.
    Question: Array delete operation, next ele replace slot,return number of eles are != val
    Topic: Two pointer
"""
def removeElement(self, nums: List[int], val: int) -> int:
    slow, fast = 0, 0 # slow: track != val and return it, fast keep whole list
    while fast < len(nums):
        if nums[fast] != val:
            nums[slow] = nums[fast]
            slow += 1
        fast += 1
    return slow
    
"""
    27.
    Question: Remove in-place many duplicates in sorted array 
    Topic: two pointer, slow track!dup
    i Compare to i-1 to determine if dup
"""
def removeDuplicates(self, nums: List[int]) -> int:
    slow = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i-1]:
            # cur diff as prev, not dup
            nums[slow] = nums[i]
            slow += 1
    return slow



"""
    80.
    Question: Return length of sorted array which val appear at most twice
    Remove duplicates in-place think two pointer
"""
def removeDuplicates(self, nums: List[int]) -> int:
    slow = 1 # counted once
    count = 1 # count first val
    for i in range(1, len(nums)):
        if count < 2 and nums[i] == nums[i-1]:
            nums[slow] = nums[i]
            slow += 1
            count += 1
        elif nums[i] != nums[i-1]:
            nums[slow] = nums[i]
            slow += 1
            count = 1
        else:
            continue
    return slow
    
