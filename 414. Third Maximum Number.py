class Solution:
    """
    return third maximum
    """
    def thirdMax(self, nums: List[int]) -> int:
        # 1SOLUTION sort
        ls = sorted(list(set(nums)), reverse=True)
        if len(ls) < 3:
            return ls[0]
        else:
            return ls[2]
        # 2SOLUTION:remove
        nums =set(nums) 
        if len(nums) < 3:
            return max(nums)
        else:
            nums.remove(max(nums))
            nums.remove(max(nums))
            return max(nums)