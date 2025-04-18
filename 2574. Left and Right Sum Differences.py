class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        """
        SOLUTION1:prefix, suffix
        STEP:no need to create two leftsum, rightsum;check their relation
        TIME:O(n) SPACE: O(1)exclude res array
        """
        res = []
        prefix = 0
        suffix = sum(nums)

        for n in nums:
            prefix += n
            res.append(abs(prefix-suffix))
            suffix -= n
        return res
