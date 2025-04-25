class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        """
        SOLUTION1: hashmap
        create three maps, freqmap={n:freq}, first={n:i}, last={n:i}keep update i then get last index
        """
        freq = defaultdict(int)
        first, last = {}, {}

        for i, v in enumerate(nums):
            if v not in first:
                first[v] = i
            last[v] = i
            freq[v]+= 1
        
        # degree value
        degree = max(freq.values())
        candidates = [k for k, v in freq.items() if v == degree]
        res = float('inf')
        for p in candidates:
            fi = first[p]
            li = last[p]
            res = min(res, li-fi+1)
        return res

