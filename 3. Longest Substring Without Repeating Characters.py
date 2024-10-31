class Solution:
    """
    Question: longest substring(consecutive) without repeating characters(ASCII 256)
    Sliding window
    1.arr store 256 char, see/kick +/-
    2.define l, r, use r to track whole string, l for shirnk window
    3.return max length of substring: r-l+1
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0
        # create arr to store char's freq
        seen = [0] * 256
        # define left, right of window
        l, r = 0, 0
        res = 0

        # use r to track string
        while r < len(s):
            # add cur char, update seen
            seen[ord(s[r])] += 1

            # resize window if s[r] occur >=1 in cur substring
            while l <= r and seen[ord(s[r])] > 1:
                # remove left from seen
                seen[ord(s[l])] -= 1
                # move on left pointer
                l += 1
            
            # get max length of unique substring
            res = max(res, r-l+1)
            # move on right pointer
            r += 1
        
        return res

