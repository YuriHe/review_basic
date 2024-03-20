class Solution:
    """
    Question: Number of matching subsequences of s
    e.g."ace" is subsequence of "abcde"
    all chars in subsequence must in s
    ISSUE: duplicate, cause TLE, so use Set store pass, nopass
    """
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        # use two sets store pass, no pass avoid visiting twice for this both
        res = 0
        pas = set()
        nopass = set()

        for word in words:
            # pre-check all failover
            if word in nopass:
                continue
            if word in pas:
                res += 1
                continue
            if len(word) > len(s): # subsequence cannot longer than s
                continue
            # check word use TWO POINTER
            i, j = 0, 0
            # iterate word and s at the same time
            while i < len(s) and j < len(word):
                if s[i] == word[j]:
                    # find one char
                    j += 1
                i += 1
            # done whole s, check if finish whole word
            if j == len(word): # mean find subsequence
                res += 1
                pas.add(word)
            else:
                nopass.add(word)
        return res
                    
        