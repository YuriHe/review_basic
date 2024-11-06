"""
Given a non-empty string word and an abbreviation abbr, return whether the string matches with the given abbreviation.
A string such as "word" contains only the following valid abbreviations:
["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]
example1:
Input : s = "internationalization", abbr = "i12iz4n"
Output : true
example2:
Input : s = "apple", abbr = "a2e"
Output : false
"""
class Solution:
    """
    @param word: a non-empty string
    @param abbr: an abbreviation
    @return: true if string matches with the given abbr or false
    """
    def valid_word_abbreviation(self, word: str, abbr: str) -> bool:
        # write your code here
        if len(word) < len(abbr): return False
        wp = 0
        ap = 0
        while wp < len(word) and ap < len(abbr):
            if abbr[ap].isalpha():
                if word[wp] != abbr[ap]:
                    return False
                else:
                    wp += 1
                    ap += 1
            else:
                # it is digit in abbr
                i = ap
                while ap < len(abbr) and abbr[ap].isdigit():
                    ap += 1
                l = int(abbr[i:ap])
                if wp +l > len(word): # eg. aa, a2
                    return False
                wp = wp + l
        return True
