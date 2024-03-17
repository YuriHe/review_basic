class Solution:
    """
    Question: Find all duplicates in array which appears twice in list [1, n]
    T:O(n) and S; O(constant)
    Map will take extra space
    SOLUTION1: negation marking
    """
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for n in nums:
            if nums[abs(n)-1]< 0: # already visited
                res.append(abs(n)) # must abs, since n already reassign
            # mark it visited and reassign
            nums[abs(n)-1] *= -1
        return res