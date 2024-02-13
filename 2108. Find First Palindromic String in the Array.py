"""
    Question: return first palindromic string in list
    Topic: two pointer
"""
def firstPalindrome(self, words: List[str]) -> str:
    for word in words:
        if self.isPalindrome(word):
            return word
    return ""
    
def isPalindrome(self, str) -> bool:
    start, end = 0, len(str)-1
    while start < end:
        if str[start] != str[end]:
            return False
        else:
            start += 1
            end -= 1
    return True