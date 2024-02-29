"""
    Question: longest substring without duplicate chars
    TODO: s contains chars, symbol, space,need to consider ALL chars
    Topic: Sliding window
"""
def lengthOfLongestSubstring(self, s: str) -> int:
    # s contains chars, symbol, space
    letter_dic = [0] * 256
    # track startpoint of window
    start = 0
    res = 0
    for i in range(len(s)):
        # first counted it, update dict
        letter_dic[ord(s[i])] += 1

        # duplicate in window
        while letter_dic[ord(s[i])] > 1:
            letter_dic[ord(s[start])] -= 1
            start += 1
        res = max(res, i - start + 1)
    return res
