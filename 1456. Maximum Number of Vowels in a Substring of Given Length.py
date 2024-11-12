class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel = ["a", "e", "i", "o", "u"]
        res = 0
        # default count
        for i in range(k):
            if s[i] in vowel:
                res += 1

        l, r = 0, k
        ctn = res
        while r < len(s):
            if s[r] in vowel:
                ctn += 1
            r += 1

            if s[l] in vowel:
                ctn -= 1
            l += 1

            res = max(res, ctn)

        return res 

        
