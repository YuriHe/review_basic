"""
409. Longest Palindrome
1.all even 2.if many odd appear, all even + all (odd-1) + 1
"""
def longestPalindrome(self, s: str) -> int:
    ctn = collections.Counter(s)
    find_mid = False
    res = 0
    for key, v in ctn.items():
        if v % 2 == 0:
            res += v
        else:
            res += (v-1)
            find_mid = True
    if find_mid:
        res += 1
    return res


"""
266. Palindrome Permutation
@param s: the given string
@return: if a permutation of the string could form a palindrome
"""
def can_permute_palindrome(self, s: str) -> bool:
    # all even or even + only one odd
    ctn = collections.Counter(s)
    ctn_odd = False
    for key, v in ctn.items():
        if v % 2 != 0:
            if not ctn_odd:
                ctn_odd = True
            else:
                # invalid
                return False
    return True



"""
5. Longest Palindromic Substring
1.aba 2.abba
use expand around center method
"""
def longestPalindrome(self, s: str) -> str:
    res = ""
    max_len = 0

    for i in range(len(s)):
        # Check for an odd-length palindrome centered at s[i]
        odd_str = self.helper(s, i, i)
        even_str = ""
        if i != len(s) -1:
            # Check for an even-length palindrome centered at s[i]
            even_str = self.helper(s, i, i+1)
        for pa in [odd_str, even_str]:
            if len(pa) > max_len:
                # update longest str
                res = pa
                # update max
                max_len = len(pa)

    return res
        
def helper(self, s, left, right) -> str:
    """
    Expands around the given center to find the longest palindromic substring.
    Returns the longest palindrome found from the given center.
    """
    while left >= 0 and right < len(s) and s[left] ==s[right]:
        left -= 1
        right += 1
    return s[left+1:right]