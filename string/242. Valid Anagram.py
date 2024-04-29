"""
    Question: Validate if Anagram
    T: O(n) S: O(n)
"""
def isAnagram(self, s: str, t: str) -> bool:
    letters = [0] * 26
    # iterfate s and count letter, add freq
    for c in s:
        letters[ord(c) - ord("a")] += 1
    # iterate t, deduct freq
    for c in t:
        if letters[ord(c) - ord("a")] <= 0:
            # c not exist in s
            return False
        else:
            letters[ord(c) - ord("a")] -= 1
    # check if all letter' value 0
    for i in range(len(letters)):
        if letters[i] > 0:
            return False
    return True