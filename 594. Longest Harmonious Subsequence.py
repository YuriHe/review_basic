class Solution:
    def findLHS(self, nums: List[int]) -> int:
        """
        SOLUTION1: hashmap
        use map store{n:freq}, iterate dict, check if key-1 exit and key+1 exit, compare then udpate longest
        """
        res = 0
        ctn = collections.Counter(nums)
        for k, v in ctn.items():
            if k-1 in ctn:
                res = max(res, v+ctn[k-1])
            if k+1 in ctn:
                res = max(res, v+ctn[k-1])
        return res
