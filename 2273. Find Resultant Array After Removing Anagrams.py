class Solution:
    """
    Question: remove adjacent anagrams
    TODO:
    1.how to handle anagram -> sort string make them same if anagram
    2.start from end of list, first index is -1, not 0
    """
    def removeAnagrams(self, words: List[str]) -> List[str]:
        res = words.copy()
        flag = ''.join(sorted(words[-1]))
        for i in range(len(words)-1, 0, -1):  # first index is -1
            prev = ''.join(sorted(words[i-1]))
            if prev == flag:
                # remove cur from res
                res.remove(words[i])
            else:
                flag = prev
        return res
