import re
class Solution:
    """
    Palindrome only consider alphanumeric characters(number+letters)
    """
    def isPalindrome(self, s: str) -> bool:
        # Solution1 Regualr Expression re.sub(pattern, replacement, string)]
        ds = re.sub("[^a-zA-Z0-9]", "", s.lower())
        return ds == ds[::-1]

        # Solution2 Builtin T O(n) S I O(n)
        s1 = ""
        for c in s:
            if c.isalnum():
                s1 += c.lower()
        return s1 == s1[::-1]

        s1 = "".join(c.lower() for c in s if c.isalnum())
        return s1 == s1[::-1]

        # Solution3 two pointer
        l = 0
        r = len(s) - 1
        while l < r:
            # skip all non-alnumeric
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            # after skip, but still have mismatch, return false
            if s[l].lower() != s[r].lower():
                return False
            else:
                l += 1
                r -= 1
        return True
            



        