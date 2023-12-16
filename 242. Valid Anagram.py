'''
QUESTION: rearrange letter, order doesn't matter. all are lowercases(26 letters)
FOLLOWUP: unicode character U+0041
'''

# SOLUTION1: use map
# TIME: n, SPACE: constant, but map have key-value pairs.
# FOLLOWUP works
def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t): return False
    dic = {}
    for c in s:
        if c in dic:
            dic[c] += 1
        else:
            dic[c] = 1
    
    for c in t:
        if c in dic:
            dic[c] -= 1
            if dic[c] == 0:
                del dic[c]
        else:
            return False
    return len(dic) == 0
        
# SOLUTION2: use array, save space 
def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        char_ls = [0] * 26
        for i in range(len(s)):
            char_ls[ord(s[i]) - ord("a")] += 1
            char_ls[ord(t[i]) - ord("a")] -= 1
        return all(count == 0 for count in char_ls)