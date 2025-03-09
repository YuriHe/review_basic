class Solution:
    """
    Question: similar one is 448
    [0,n],only missing one
    """
    def missingNumber(self, nums: List[int]) -> int:
        # 1SOLUTION: use set to achieve O(1). but space O(n)
        ns = set(nums)
        start = 0
        while start <= len(nums):
            if start not in ns:
                return start
            start += 1
        return -1

        # 2SOLUTION:XOR (best)
        """
        b^b=0
        a^0=a
        apply XOR operatioon to both index and value.
        index=val
        """
        res=len(nums)
        for i in range(len(nums)):
            res ^= i ^ nums[i]
        return res

        # 3SOLUTION:sum
        total = sum(list(range(len(nums)+1)))
        curSum = sum(nums)
        return total - curSum

        # 4SOLUTION: Brute force, T: O(n^2) S: O(1)
        for i in range(len(nums)+1):
            if i not in nums:
                return i
        return -1
            