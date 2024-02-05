"""
    Question: return index of char which is first unique in list
    Topic: Counter, hashmap
"""
def firstUniqChar(self, s: str) -> int:
    # Solution1 builtin T:O(n^2)
    # for i, v in enumerate(s):
    #     if s.count(v) == 1:
    #         return i
    # return -1
    # Solution2 Counter T:O(n^2)
    # count = Counter(s)
    # for i in range(len(s)):
    #     if count[s[i]] == 1:
    #         return i
    # return -1
    # Solution3 set, map, T: O(n)
    seen = set()
    uniq_dic = {}
    for i, v in enumerate(s):
        if v not in seen: 
            seen.add(v)
            uniq_dic[v] = i
        elif v in uniq_dic: # must have otherwise no foun keu
            # duplicate
            del uniq_dic[v]
    # compare index when value appear once 
    return min(uniq_dic.values()) if uniq_dic else -1
