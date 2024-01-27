"""
    Question: Palindrom which only letter and number
    Solution1: built-in function T:O(n) S:O(n)
    Solution2: two pointer
    Topic:
    char.isalnum()-> bool
    s=s.strip()
"""
def isPalindrome(self, s: str) -> bool:
    # Solution1
    s1 = ""
    for c in s:
        if c.isalnum():
            s1 += c.lower()
    return s1 == s1[::-1]
    # Solution1.1
    s1= "".join(c.lower() for c in s if c.isalnum())
    return s1 == s1[::-1]
    # Solution2
    l = 0
    r = len(s)-1
    while l < r: # last compare between two char
        while l<r and not s[l].isalnum():
            l += 1
        while l<r and not s[r].isalnum():
            r -= 1  
        if s[l].lower() != s[r].lower():
            return False
        l += 1
        r -= 1
    return True
        
        
print(isPalindrome("  23\"f6??6f\"32LL"))