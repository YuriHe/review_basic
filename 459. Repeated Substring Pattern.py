class Solution:
    """
    QUESTION: check string if made by repeated pattern 
    must repeat >= 2times, so use s+s, remove first and last char, get s2, see if s in s2;  will overlap if have repeat pattern
    """
    def repeatedSubstringPattern(self, s: str) -> bool:
        s1 = s+s
        s2 = s1[1:-1]
        return s in s2