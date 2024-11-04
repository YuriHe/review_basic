class Solution:
    """
    Question: input is rotated sorted array, can separate two sorted array,
    O(logn) binary search
    """
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums)-1
        while low <= high:
            mid = (low+high) // 2
            if nums[mid] == target:
                return mid
            elif nums[low] <= nums[mid]: # this part is sorted
                if nums[low] <= target and target <= nums[mid]:
                    # shrink rage
                    high = mid - 1
                else:
                    low = mid + 1
            else: # across rotate subarray
                if nums[mid] <= target and target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid -1
        return -1
