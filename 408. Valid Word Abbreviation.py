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
"""
Question: verify if abbreviation string of word string
Step1:two pt track both,handle digits of abrr
"""
    def verify(word, abbr):
    if len(word) < len(abbr): return False
    
    wp, ap = 0, 0
    while ap < len(abbr):
        if abbr[ap].isalpha(): # match letter
            if wp >= len(word) or abbr[ap] != word[wp]:
                return False
            wp += 1
            ap += 1
        elif abbr[ap].isdigit(): # handle digits
            # leading zero check
            if abbr[ap] == '0':
                return False
            
            # extract full number
            tmp = ""
            while ap < len(abbr) and abbr[ap].isdigit():
                tmp += abbr[ap]
                ap += 1
            wp += int(tmp)
            
            if wp > len(word):
                return False
        else:
            return False
            
    return wp == len(word)
    
print(verify("internationalization", "i12iz4n"))  # Output: True
print(verify("apple", "a2e"))  # Output: False
print(verify("apple", "a3e"))  # Output: True
print(verify("apple", "a01e"))  # Output: False
print(verify("apple", "a55"))
print(verify("apple", "a0pple"))