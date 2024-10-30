"""
    Question:search target which may duplicate in sorted list
    Topic:binary search O(logn)
"""
def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums)-1
        # nums=[3] target=3, [0,0] so <=
        while l <= r:
            mid = (l + r) //2
            if nums[mid] == target:
                # find target, expand to left and right
                l = mid - 1
                r = mid + 1
                while l >= 0 and nums[l] == target:
                    l -= 1
                while r < len(nums) and nums[r] == target:
                    r += 1

                return [l+1, r-1]
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return [-1, -1]