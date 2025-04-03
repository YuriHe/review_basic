class Solution:
    """
    QUESTION: verify if Isomorphic string with each other
    """
    def isIsomorphic(self, s: str, t: str) -> bool:
        """
        SOLUTION1: Dictionary
        HOW: create two Dict and iterate strings, if any not match return False
            s="badc",t="baba"
        TIME: O(N), SPACE: O(N)
        """
        if len(s) != len(t): return False

        sDict, tDict = {}, {}
        for i in range(len(s)):
            if s[i] not in sDict:
                sDict[s[i]] = t[i]
            else:
                if sDict[s[i]] != t[i]:
                    return False
                
        for i in range(len(t)):
            if t[i] not in tDict:
                tDict[t[i]] = s[i]
            else:
                if tDict[t[i]] != s[i]:
                    return False

        return True
