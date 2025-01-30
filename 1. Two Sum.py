class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        1.Solution: hashmap one pass: {num: i} 
        Time: O(n) Space: O(n)
        """
        dic = {}
        for i, n in enumerate(nums):
            first = target - n
            if first in dic:
                return [dic[first], i]
            else:
                dic[n] = i
        return [-1, -1]