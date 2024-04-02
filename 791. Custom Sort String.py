from collections import Counter
class Solution:
    """
    Question: return string , but sort s based on order 
    """
    def customSortString(self, order: str, s: str) -> str:
        # store s (char, freq) into map
        s_map = Counter(s)
        res = ""
        # sort s based on order, delete isited char in order
        for c in order:
            if c in s_map:
                times = s_map[c]
                res += c * times
                del s_map[c]

        # add extra char in s, but no include in order
        for c, freq in s_map.items():
            res += c * freq
        return res


