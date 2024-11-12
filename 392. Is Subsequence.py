class Solution:
    """
    392. Is Subsequence
    Question subsequence, but substring
    Check if s is subsequence of t
    Scan s, t together, no need to store hashmap{ch: idx}
    """
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t): return False
        i, j = 0,0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                # found
                i += 1
                j += 1
            else:
                # keep searching from t
                j += 1
        
        return i == len(s)