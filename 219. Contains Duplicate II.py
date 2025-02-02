class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """
        1.Solution: brute force, iterate i, then j (TLE )
        Time: O(n^2), Space O(1)
        """
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)): # distinc index
                if abs(i-j) <= k:
                    if nums[i] == nums[j]:
                        return True
                else:
                    break
        return False
        """
        2.Solution:hashmap {num:[i1, i2]}
        Time: O(n) Space: O(n)
        """
        dic = collections.defaultdict(list)
        for i, n in enumerate(nums):
            if n in dic:
                # find duplicate, compare cur to last index distance
                if i - dic[n][-1] <= k:
                    return True
            dic[n].append(i)
        return False
