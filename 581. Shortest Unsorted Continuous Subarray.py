class Solution:
    """
    Question: shortest unsorted consecutive subarray
    e.g. [3,6,4,8,1,9,15]-> [3,6,4,8,1,9]
    SOLUTION1: SORT T:O(nlogn)
    """
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        # SOLUTION1: sort, and find difference of index
        sorted_arr = sorted(nums)
        diff = []
        for i in range(len(sorted_arr)):
            if sorted_arr[i] == nums[i]:
                continue
            else:
                diff.append(i)
        return max(diff)-min(diff)+1 if diff else 0

            