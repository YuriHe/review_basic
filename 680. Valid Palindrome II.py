class Solution:
    def validPalindrome(self, s: str) -> bool:
        # abbccda no sure which one need to delete so use reusable function ispalindrome to check
        if not s or len(s) <= 1: return True
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                break
        # now need delete one
        if self.isPalindrome(s, left+1, right) or self.isPalindrome(s, left, right-1):
            return True
        else:
            return False

    # Ask if string[i:j] is palindorme
    def isPalindrome(self, s, i, j):
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
