class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        # return number of unqiue palindrome subsequence with len3
        # i,k,j, confirm same value but at leftmost and rightmost index, count between set length
        letters = set(s)
        res = 0
        for letter in letters:
            i, j = s.index(letter), s.rindex(letter)
            between = set()
            for k in range(i+1, j):
                between.add(s[k])
            res += len(between)
        return res
