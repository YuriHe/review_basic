class Solution:
    def countSegments(self, s: str) -> int:
        # SOLUTION1: built-in function, split() will remove any long space, divide str to arr
        return len(s.split())
        # SOLUTION2:
        ct = 0 # keep track of number of segments in input string
        # iterate string character by character
        for i in range(len(s)):
            # check if new segment
            if s[i] != ' ' and ( i== 0 or s[i-1] ==' '):
                ct += 1
        return ct