class Solution:
    """
    Question: Find all numbers are missing in array, which also means duplicates
    SOLUTION: Intuitive way S: O(n)
    """
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        set_n = set(nums)
        res = []
        for idx in range(1, len(nums)+1):
            if idx not in set_n:
                res.append(idx)
        return res
        