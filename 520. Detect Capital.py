class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        # SOLUTION1: native solution
        upper_ct,lower_ct = 0, 0
        for c in word:
            if c == c.upper():
                upper_ct += 1
            else:
                lower_ct += 1
        if upper_ct == len(word):
            return True
        elif upper_ct == 0:
            return True
        elif word[0] == word[0].upper() and upper_ct == 1:
            return True
        else:
            return False
        # SOLUTION2: one line
        return word == word.upper() or word[1:] == word[1:].lower()
