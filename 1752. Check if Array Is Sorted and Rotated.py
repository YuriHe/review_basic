class Solution:
    def check(self, nums: List[int]) -> bool:
        """
        1.Solution: sorting
        Idea:try each num see if it is pivot, rotated back see if sorted list
        Time: O(n*nlogn)
        """
        for i in range(len(nums)):
            rotated = nums[i:] + nums[:i]
            if rotated == sorted(nums):
                return True
        return False
        """
        2.Solution: compare with next neighbor, only van violate at most once
        Time: O(n)
        """
        count = 0 # count order is violated
        for i in range(len(nums)):
            if nums[i] > nums[ (i+1) % len(nums)]:
                count += 1
                if count > 1:
                    return False
        return True