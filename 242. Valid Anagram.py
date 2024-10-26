from collections import Counter
class Solution:
    # handle unicode in s, t
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        dic1 = Counter(s)
        for c in t:
            if c not in dic1 or dic1[c] == 0:
                return False
            else:
                dic1[c] -= 1
        return all(count == 0 for count in dic1.values())

    # handle only lowercase letter a-z
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        char_arr = [0] * 26
        for i in range(len(s)):
            char_arr[ord(s[i]) - ord('a')] += 1
            char_arr[ord(t[i]) - ord('a')] -= 1
        return all(count == 0 for count in char_arr)
