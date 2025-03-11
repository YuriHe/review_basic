class Solution:
    def isValid(self, word: str) -> bool:
        vowels="aeiou"
        if len(word) < 3:
            return False
        
        hasV, hasC = False, False

        for c in word:
            if not c.isalnum():
                return False
            elif c.isalpha():
                if c.lower() in vowels:
                    hasV = True
                else:
                    hasC = True
        return hasV and hasC