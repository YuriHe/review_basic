"""
    Question: Longest common prefix(substring) 
    TODO: pick first val as flag, rest of vals compare to it, update flag
"""
def longestCommonPrefix(self, strs: List[str]) -> str:
    if len(strs) == 0: return ""
    flag = strs[0]
    for i in range(1, len(strs)):
        cur = strs[i]
        check_len = min(len(flag), len(cur))
        j = 0
        while j < check_len and flag[j] == cur[j]: # check each char in str
            j += 1
        # update flag
        flag = flag[:j]
    return flag
        