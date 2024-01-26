"""
    Question: find index of substring(needle)which may appear few times in haystack
    Solution1: built-in use .find  return -1 not found; .index will ValueError not found
    Solution2: two pointer
    Issue: boundary
"""
def strStr(self, haystack: str, needle: str) -> int:
    # Solution1
    # return haystack.find(needle)
    # Solution2
    if len(haystack) < len(needle): return -1
    i = 0 # track needle
    n_l = len(needle)
    for j in range(len(haystack)):
        if j+n_l <= len(haystack) and haystack[j:j+n_l] == needle:
            return j
    return -1
