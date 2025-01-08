class Solution:
    """
    33. Search in Rotated Sorted Array
    Question: input is rotated sorted array, can separate two sorted array,
    O(logn) binary search
    """
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums)-1
        while low <= high:
            mid = (low+high) // 2
            if nums[mid] == target:
                return mid
            # left part is sorted, low index can = mid index
            elif nums[low] <= nums[mid]:
                if nums[low] <= target and target <= nums[mid]:
                    # shrink rage
                    high = mid - 1
                else:
                    low = mid + 1
            # right part is sorted
            else:
                if nums[mid] <= target and target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid -1
        return -1


class Solution:
    """
    153. Find Minimum in Rotated Sorted Array 
    No matter rotate times 
    compare nums[mid] with nums[right]
    """
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        while left < right:
            mid = left + (right-left)//2
            if nums[mid] > nums[right]:
                # smaller on the right of mid
                left = mid + 1
            else:
                right = mid
        return nums[right]
