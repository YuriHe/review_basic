class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        1.Solution: Convert list then sort and compare
        Time:O(nlogn) Space: O(n)
        """
        if len(s) != len(t): return False
        arrS = sorted(list(s))
        arrT = sorted(list(t))
        return arrS == arrT
        """
        2.Solution: hashmap handle all unicode
        Time:O(n) Space: O(n)
        """
        dictS = collections.Counter(s)
        for c in t:
            if c not in dictS or dictS[c] <= 0:
                return False
            dictS[c] -= 1
        return all(v == 0 for k, v in dictS.items())
        """
        3.Solution: hashmap,If input only include lowercase
        Idea:Already handled who is larget set, if s larger, return statement handle; if t larger,ctn[char]handle
        Time:O(n) Space: O(n)
        """
        ctnS = [0] * 26
        for c in s:
            ctnS[ord(c)-ord('a')] += 1
        for c in t:
            if ctnS[ord(c)-ord('a')] <= 0:
                return False
            ctnS[ord(c)-ord('a')] -= 1
        return all(ctnS[i] == 0 for i in range(len(ctnS)))