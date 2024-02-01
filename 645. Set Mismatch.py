"""
    Question: In array[1..n] consecutive integers return[duplicate, miss] 
    Issue: [2,2] -> [2,1]
    Solution1: brute force T: O(n^2) S:O(1)
"""
def findErrorNums(self, nums: List[int]) -> List[int]:
    # Solution1
    dup, miss = -1, -1
    # iterate from 1 to n
    for n in range(1, len(nums)+1):
        # use .count function which cause T:O(n)
        c = nums.count(n)
        if c == 2:
            # find dup
            dup = n
        elif c == 0:
            # find miss
            miss = n
    return [dup, miss]