class Solution:

    def encode(self, strs: List[str]) -> str:
        """
        1.Solution: serialize list of string to string
        Idea:convert the length of the string into a fixed 4-digit string, (strs[i].length<200)
        add the string itself, and append it to the result string in sequence.
        T: O(n)
        """
        res = []
        for s in strs:
            # if num length 4, will fill with 4 length and right align, if left-align f"{len(s):<4}" + s
            res.append(f"{len(s):4}" + s) # jie. _ _ _3jie
        return ''.join(res)

    def decode(self, s: str) -> List[str]:
        """
        1.Solution: deserialize string to list of string
        Idea:extra length of string, and move pointer
        T: O(n)
        """
        i, n = 0, len(s)
        res = []
        while i < n:
            size = int(s[i:i+4])
            i += 4
            # char at i+4
            res.append(s[i: i+size])
            i += size
        return res
