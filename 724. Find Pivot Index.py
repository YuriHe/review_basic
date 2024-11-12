class Solution:
    """
    Question: find pivot index, leftsum = rightsum otherwise return -1
    check leftsum == total - leftsum -cur
    """
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        leftsum = 0

        for i, n in enumerate(nums):
            if leftsum == total - n - leftsum:
                return i
            leftsum += n
        return -1
        