"""
    Question: find longest consecutive sequence
    SOLUTON1:sort O(nlogn)
    SOLUTION2:use hashset to confirm if cur-1 exist or not, if not, this is start of sequence
"""
def longestConsecutive(self, nums: List[int]) -> int:
    # can be duplicates
    res = set(nums)
    longest = 0

    # check if cur-1 exist
    for n in res:
        if n-1 not in res:
            # n is start of sequence
            l = 1
            # consecutive num keep modifying
            while (n+l) in res:
                l += 1
            longest = max(longest, l)
        
    return longest
            