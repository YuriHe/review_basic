class Solution:
    def balancedStringSplit(self, s: str) -> int:
        """
        SOLUTION1: traverse string
        return max number of balance substring means shortest length of each substring
        seeR++,seeL--,if 0 ++
        TIME: O(N)
        """
        see = 0
        res = 0
        for c in s:
            if c == "R":
                see += 1
            else:
                see -= 1
            if see == 0:
                res += 1
        return res