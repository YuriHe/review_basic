class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        # A string is always a subsequence of itself
        # what is subsequence? A subsequence（子序列） is a sequence that can be derived from another sequence by deleting some or no characters without changing the order of the remaining characters. eg.S=abcde, valid subsequence: ace,abc,a,''
        if a == b: return -1
        return max(len(a), len(b))