class Solution:
    """
    Question:
    sort list
    return sum 
    check which sum-target is smaller
    """
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # three points, fix 1 num, and handle 2 and 3 ,update res 
        # no consider index, so can sort
        resSum = nums[0] + nums[1] + nums[2]
        nums.sort()

        for i in range(len(nums)-2):
            first = nums[i]
            left, right = i+1, len(nums)-1
            while left < right:
                tmpSum = first + nums[left] + nums[right]
                if abs(tmpSum-target) == 0:
                    return tmpSum
                # see resSum or tmpSum is closer
                if abs(tmpSum-target) < abs(resSum-target):
                    resSum = tmpSum
                # move pointer
                if tmpSum > target:
                    # too larger, find smaller
                    right -= 1
                elif tmpSum < target:
                    left += 1
        return resSum