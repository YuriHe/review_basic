class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            if haystack[i] == needle[0]: # find first char of needle
                l = len(needle)
                if haystack[i:i+l] == needle:
                    return i
        return -1
