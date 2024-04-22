"""
    Question: List of List which group anagrams
    Topic: {sortedword: [group items]}, return [[group items]]
    No need to set flag
"""
def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    if strs == [""]: return [[""]]
    dic = {}
    for s in strs:
        # convert string to array, then sort, then convert back to string
        key = "".join(sorted(list(s)))
        if key not in dic:
            dic[key] = []
        dic[key].append(s)
    return dic.values()