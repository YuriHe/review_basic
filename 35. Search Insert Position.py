"""
    Question: Search & insert in sorted list
    T: logn S: 1
    [1,3,5,6] target:2 mid=3
    -> [1,3] mid=0
    -> low=1, high=0
"""
def searchInsert(self, nums: List[int], target: int) -> int:
    low, high = 0, len(nums)-1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target: return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return low