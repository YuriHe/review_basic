"""
    205. Isomorphic Strings
    Question:char in s can map to/form char in t onetime, order not matter
    Topic: Two Hashmap, store char in each other's map {char, opponent's char}
    Issue: s="aba" t="rrr" should bijection
    Solution1: two hashmap T: O(n) s: O(n)
    """
def isIsomorphic(self, s: str, t: str) -> bool:
    if len(s) != len(t): return False
    s_map, t_map = {}, {}
    # store to hash and also compare 
    for i in range(len(s)):
        if s[i] not in s_map:
            s_map[s[i]] = t[i]
        else:
            if s_map[s[i]] != t[i]: return False
    for i in range(len(t)):
        if t[i] not in t_map:
            t_map[t[i]] = s[i]
        else:
            if t_map[t[i]] != s[i]: return False
    return True

"""
    290. Word Pattern
    Question: bijection between each char in two strings
    Solution1: use two hashmap
"""
def wordPattern(self, pattern: str, s: str) -> bool:
    arr = s.split(" ") # no any leading or trailing spaces
    if len(pattern) != len(arr): return False
    p_map, s_map = {}, {}
    for i in range(len(pattern)):
        if pattern[i] not in p_map:
            p_map[pattern[i]] = arr[i]
        else:
            if p_map[pattern[i]] != arr[i]: return False
    for i in range(len(arr)):
        if arr[i] not in s_map:
            s_map[arr[i]] = pattern[i]
        else:
            if s_map[arr[i]] != pattern[i]: return False
    return True
                
        

