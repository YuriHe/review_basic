"""
    Question: find first bad version 
    Topic: Binary search
    Issue: <= or <, return lower/upper bound eg.[1,2] 2
"""
def firstBadVersion(self, n: int) -> int:
    low, high = 1, n
    while low < high:
        mid = (low+high-1)//2
        if isBadVersion(mid):
            # maybe first one, keep track lower bound
            high = mid
        else:
            # not bad version yet, keep track to right
            low = mid + 1
    return low
        