class Solution:
    """
    greedy
    """
    def breakPalindrome(self, palindrome: str) -> str:
        # corner case single char also valid palindrome
        if len(palindrome) <= 1: return ""
        # find pos to replace, choose which character make smallest
        # check if not 'a' that is pos, choose 'a' earlier as we can 
        # input is valid palindrome, so only think half len, modify first part
        ls = list(palindrome)
        for i in range(len(palindrome)//2):
            if palindrome[i] != 'a':
                ls[i] = 'a'
                return "".join(ls)
        ls[-1] = 'b'
        return "".join(ls)
                