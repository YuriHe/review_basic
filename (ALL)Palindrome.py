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

