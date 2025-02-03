"""
    26.
    Question: Array delete operation, next ele replace slot,return number of eles are != val
    Topic: Two pointer
"""
def removeElement(self, nums: List[int], val: int) -> int:
    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k
    
"""
    27.
    Question: Remove in-place many duplicates in sorted array 
    Topic: two pointer, k track final array
    i Compare to i-1 to determine if dup
"""
def removeDuplicates(self, nums: List[int]) -> int:
    k = 0
    for i in range(1, len(nums)):
        if nums[i] != nums[k]:
            k += 1
            nums[k] = nums[i]
    return k+1 if len(nums) > 0 else 0

"""
    80.
    Question: Return length of sorted array which val appear at most twice
    Remove duplicates in-place think two pointer
"""
def removeDuplicates(self, nums: List[int]) -> int:
        # compare duplicate, start from index1
        # use count variable to count occurance of elements
        count = 1
        # use k track final array
        k = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[k]:
                # replace and reset count
                k += 1
                nums[k] = nums[i]
                count = 1
            else:
                if count < 2:
                    k += 1
                    nums[k] = nums[i]
                    count += 1
                else:
                    continue
                
        return k+1 if len(nums) > 0 else 0
