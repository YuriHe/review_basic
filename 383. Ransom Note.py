"""
    Question:if all char in A are all in B  B.len>A.len, order doesn't matter
    Solution1: use Counter
"""
def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    # Solution1:
    if len(ransomNote) > len(magazine): return False
    map_count = Counter(magazine)
    for c in ransomNote:
        map_count[c] -= 1
        if map_count[c] < 0: return False
    return True