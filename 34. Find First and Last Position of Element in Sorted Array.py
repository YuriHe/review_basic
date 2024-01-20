"""
    Question:search target which may duplicate in sorted list
    Topic:binary search
    Issue: ifinite loop-> check variable name is correct
"""
def searchRange(self, nums: List[int], target: int) -> List[int]:
        start, end = 0, len(nums)-1
        while start <= end:
            mid = (start+end) // 2
            if nums[mid] == target:
                # restore mid index to start/end
                # do -1/+1 can check 1num and prepare while loop
                if mid-1 >= 0: 
                    start = mid-1
                if mid+1 < len(nums):
                    end = mid+1
                # found part of substring we need and spread two sides
                while start >= 0 and nums[start] == target:
                    start -= 1
                while end < len(nums) and nums[end] == target:
                    end += 1
                return [start+1, end-1]
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return [-1,-1]