"""
    Question: Rotate array in-place
    Two pointers to track index 
    Rotate count may > len, so use k % n = k
"""
def rotate(self, nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    k = k % n
    # 1step Rotate entire list
    self._swap(nums, 0, n-1)
    # 2step Rotate first k elements
    self._swap(nums, 0, k-1)
    # 3step Rotate rest of list starting from k index
    self._swap(nums, k, n-1)


# helper func
def _swap(self, ls: List[int], start: int, end: int) -> None:
    while start < end:
        ls[start], ls[end] = ls[end], ls[start]
        start += 1
        end -= 1