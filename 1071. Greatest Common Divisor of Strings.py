class Solution:
    """
    Question: find largest common division
    1.find largest base can be common for both string and base keep changing use pointer moving
    2.verify cur base is match or not, if not i -=1
    """
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        l1, l2 = len(str1), len(str2)
        def verify(k) -> bool:
            if l1 % k != 0 or l2 % k != 0:
                return False

            base = str1[:k]
            return base * (l1 // k) == str1 and base * (l2 // k) == str2

        for i in range(min(len(str1), len(str2)), 0, -1):  
            if verify(i): # mean substr[:i] this base match
                return str1[:i]
        return ""
        