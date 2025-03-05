class Solution:
    """
    Question: return number of palindrome substring
    """
    def countSubstrings(self, s: str) -> int:
        """
        SOLUTION2: Two pointer BEST
        Use center expand method
        TIME:O(n^2)
        """
        def _expand(left, right):
            count = 0
            while left >=0 and right < len(s) and s[left]==s[right]:
                count += 1
                left -=1
                right +=1
            # now left and right is not invalid, shrink str
            return count
        
        total = 0

        for i, c in enumerate(s):
            total += _expand(i,i)
            total += _expand(i,i+1)
        return total

        """
        SOLUTION1: Brute force TLE
        STEP:iterate string, find substring[i:], then verify if substring is palindrome (n^3)
        TIME:O(n^3)
        """
        res = 0
        
        for i in range(len(s)):
            for j in range(i, len(s)):
                l, r = i, j
                while l < r and s[l] == s[r]:
                    l += 1
                    r -= 1
                res += (l >= r)
                
        return res