class Solution:
    """
    Return T/F if swap chars in two strings and make them close.swap is unlimited
    Issue: No need to make them same, just same pattern; should have char appear in both
    T: nologn
    S: 2N
    TODO: Counter, and values list are same in both words, then mean close,can swap anything
    """
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2) or set(word1) != set(word2):
            return False
        w1_map = Counter(word1)
        w2_map = Counter(word2)
        return sorted(w1_map.values()) == sorted(w2_map.values())
        