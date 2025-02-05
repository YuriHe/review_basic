class Solution:
    # 80. Remove Duplicates from Sorted Array II
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        1.Solution:two pointer one pass and modify input nums array
        Time: O(n)
        """
        count = 1 # at most 2
        k = 1 # track final result length of nums array
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                # reset count
                nums[k] = nums[i]
                k += 1
                count = 1
            else:
                if count < 2:
                    nums[k] = nums[i]
                    k += 1
                    count += 1
                else: 
                    continue
        return k
