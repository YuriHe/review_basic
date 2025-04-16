class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        """
        SOLUTION1: iterate array + hashmap make n^2 to n
        eg.[1,1,1]->3
        TIME: n
        """
        count = 0
        pair = collections.defaultdict(int)
        if len(nums) < 2: return res

        for i in range(len(nums)):
            if nums[i] in pair:
                count += pair[nums[i]]
            pair[nums[i]] += 1
        return count

