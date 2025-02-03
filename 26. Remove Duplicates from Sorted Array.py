class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        1.Solution:two pointer, moving in-place
        Idea:since sorted, compare to neighbor and update input nums array
        Time: O(n), Space: O(1)
        """
        k = 0
        res = 1
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                k += 1
                nums[k] = nums[i]
        return k+1
