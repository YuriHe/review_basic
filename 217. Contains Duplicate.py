from collections import Counter
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        1.Solution:hashmap
        Time:O(n), Space:O(n) store key-value pair
        """
        ctn = Counter(nums)
        return any(v > 1 for k, v in ctn.items())
        """
        2.Solution:hashset
        Time:O(n), Space:O(n)
        """
        return len(set(nums)) != len(nums)