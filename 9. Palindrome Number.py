"""
    Question: use Math way to check integer is palindrome
"""
def isPalindrome(self, x: int) -> bool:
    if x < 0: return False
    # copy x, keep x
    copy = x
    res = 0
    while copy > 0: 
        # template iterate each digit
        res = res * 10 + copy % 10
        copy //= 10
    return x == res
    