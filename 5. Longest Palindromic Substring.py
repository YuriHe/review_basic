class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        SOLUTION1: Two pointer
        two cases:aba,aa
        STEP: when iterate string, each value will try do center expand(helper) 
        TIME: O(n^2)S SPACE:O(1)
        """
        def _expand(left, right):
            while left >=0 and right < len(s) and s[left]==s[right]:
                left -=1
                right +=1
            # now left and right is not invalid, shrink str
            return s[left+1:right]

        max_len, res = 0, ""

        for i, c in enumerate(s):
            odd_str = _expand(i, i)
            even_str = _expand(i, i+1)
            
            ls = [odd_str, even_str]
            for word in ls:
                if len(word) > max_len:
                    # update res
                    max_len=len(word)
                    res = word
            
        return res
