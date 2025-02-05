class Solution:
    # 128. Longest Consecutive Sequence
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        1.Solution:set + sorting + two pointer
        Idea: sort hashset (1,2,0,1), then update max_len
        Time: O(nlogn) Space: O(1)
        """
        max_len = 0
        nums = set(nums)
        # consider corner case
        if len(nums) <= 1: return len(nums)
        nums = sorted(set(nums))
        left = 0
        # below handle >=2 ele
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                continue
            else:
                max_len =max(max_len, i-1-left+1)
                left = i
        if left != len(nums)-1:
            max_len = max(max_len, len(nums)-1-left+1)
        return max_len
        """
        1.Solution:hashset
        Idea: iterate numset, verify if it is first num in consecutive sequence, if yes then loop for set until not exist
        Time: O(n) Space: O(n)
        """
        numSet = set(nums)
        max_len = 0 # global

        for n in numSet:
            if n-1 not in numSet:
                # n is first
                length = 1
                while (n + length) in numSet:
                    length += 1
                max_len = max(length, max_len)
        return max_len

       
        