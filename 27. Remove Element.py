"""
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
    

    
