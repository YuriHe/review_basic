"""
    Question: rearrange lowercase letter
    Topic: char()<-> ord()
    1 SOLUTION: sorted(s) == sorted(t). T:nlogn S:n
    2 SOLUTION: use map, insert-> take out T:n, S:n
    3 SOLUTION: use char array, save key-value pair space T: n, S:26
"""
def isAnagram(self, s: str, t: str) -> bool:
    # Solution2
    if len(s) != len(t): return False
    dic = {}
    for c in s:
        dic[c] = dic.get(c, 0) + 1
    for c in t:
        dic[c] = dic.get(c, 0) - 1
        if dic[c] == 0:
            del dic[c]
    return not dic
    # Solution 3
    if len(s) != len(t): return False
    char_arr = [0] * 26
    for i in range(len(s)):
        # track two lists in the same time
        char_arr[ord(s[i]) - ord("a")] += 1
        char_arr[ord(t[i]) - ord("a")] -= 1
    return all(count == 0 for count in char_arr)
