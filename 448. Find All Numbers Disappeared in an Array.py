class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # 1SOLUTION: set, S: O(n)
        ns = set(nums)
        start = 1
        res = []
        while start <= len(nums):
            if start not in ns:
                res.append(start)
            start += 1
        return res
        # 2SOLUTION; in-place marking, num mapping with index
        # [1,4,4,3] -> [-1,4,4,-4]
        # all number are positive, think negative
        res = []
        # mark existing
        for n in nums:
            # why abs, may already updated to negative
            idx = abs(n) - 1 # num:1 mapping idx:0
            nums[idx] = -1 * abs(nums[idx])
        for i, n in enumerate(nums):
            if n > 0:
                res.append(i+1)
        return res


