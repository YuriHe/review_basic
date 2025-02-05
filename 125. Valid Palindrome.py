import re

class Solution:
    # 125. Valid Palindrome
    def isPalindrome(self, s: str) -> bool:
        """
        1.Solution: regular expression
        Time: O(n)
        """
        ns = re.sub("[^a-zA-Z0-9]", "", s.lower())
        return ns == ns[::-1]
        """
        2.Solution: two pointer
        """
        left, right = 0, len(s)-1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -=1
            if s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1
        return True
        