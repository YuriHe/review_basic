"""
    Question: use Math way to check integer is palindrome
"""
def isPalindrome(self, x: int) -> bool:
    # SOLUTION1 Convert type
    if x < 0:
            # negative num
            return False
        return str(x)[::-1] == str(x)

    # SOLUTION2 handle integer
    if x < 0: return False
    # delare copy for compare if 'res' same as x in following steps
    copy = x
    res = 0
    # iterate digits in x
    while copy > 0:
        res = res * 10 + copy % 10
        copy //= 10
    return res == x