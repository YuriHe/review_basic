def groupAnagrams(strs):
    # use hash key: list of value {anagram: [s1, s2, s3]}]
    res = {}
    for s in strs:
        k = "".join(sorted(s))
        if k not in res:
            res[k] = []
        res[k].append(s)

    return list(res.values()) # must convert dict_value object to list

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))