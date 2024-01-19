"""
    Question: Search in sorted list
    Time: logn
    Issue: Avoid infinite loop and boundary issue
"""
def search(self, nums: List[int], target: int) -> int:
    low,high = 0, len(nums)-1
    while low <= high: # consider 1 
        mid = (low + high) // 2
        if nums[mid] == target: return mid
        elif nums[mid] < target: low = mid + 1 # nums[mid] won't target
        else: high = mid - 1 # nums[mid] won't target
    return -1