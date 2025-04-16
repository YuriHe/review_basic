from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        SOLUTION1: two dict
        """
        rDict = Counter(ransomNote)
        mDict = Counter(magazine)
        # iterate rDict
        for k, v in rDict.items():
            if k not in mDict or v > mDict[k]:
                return False
        return True