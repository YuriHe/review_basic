""" 278. Bad version
    Question: find first bad version 
    Topic: Binary search
    Issue: <= or <, return lower/upper bound eg.[1,2] 2
"""
def firstBadVersion(self, n: int) -> int:
    low, high = 1, n
    while low < high:  # cannot <= (infinite loop)
        mid = (low+high)//2
        if isBadVersion(mid):
            # maybe first one, keep track lower bound
            high = mid
        else:
            # not bad version yet, keep track to right
            low = mid + 1
    return low

# standard template
def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        while left <= right:
            mid = (left+right) // 2
            if isBadVersion(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left
        


""" 704.Binary search
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
