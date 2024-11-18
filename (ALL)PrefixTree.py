"""
Prefix Tree
"""
from typing import List
class TrieNode:
    def __init__(self, val=None):
        self.char = val
        self.children = {} # char: {node(char)}
        self.isEnd = False

class Trie:
    def __init__(self):
        # create root
        self.root = TrieNode(None)
    
    def insert(self, word) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode(c)
            cur = cur.children[c]
        cur.isEnd = True
    
    def search_prefix(self, prefix) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True

"""
Prefix Matching
1. Check if a String is a Prefix of Another String
Given an array of strings words, you need to determine if there exists any string in the array that is a prefix of another string.

A string is a prefix of another string if it appears at the beginning of the other string. For example, "apple" is a prefix of "applepie".

Input:
An array of strings words, containing n (1 ≤ n ≤ 1000) strings. Each string has a length of m (1 ≤ m ≤ 100) and does not exceed 100 characters.
Output:
Return true if there exists any string in the array that is a prefix of another string; otherwise, return false.
Example:
Example 1:

plaintext
Copy code
Input: words = ["apple", "app", "banana"]
Output: true
Explanation: "app" is a prefix of "apple".
Example 2:

plaintext
Copy code
Input: words = ["dog", "racecar", "car"]
Output: false
Explanation: No string is a prefix of another.
Example 3:

plaintext
Copy code
Input: words = ["a", "ab", "b", "ba"]
Output: true
Explanation: "a" is a prefix of "ab".
"""
Use sort compare adjacent:
def hasPrefix(words) -> bool:
    words.sort()
    for i in range(1, len(words)):
        if words[i].startswith(words[i-1]):
            return True
    return False

words1 = ["apple", "app", "banana"]
print(hasPrefix(words1))  # Output: True

words2 = ["dog", "racecar", "car"]
print(hasPrefix(words2))  # Output: False

words3 = ["a", "ab", "b", "ba"]
print(hasPrefix(words3))  # Output: True


"""
1268. Search Suggestions System
"""
def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
    # sort products
    products.sort()
    res = []
    prefix = ""

    for c in searchWord:
        prefix += c
        inner = []
        for p in products:
            if p.startswith(prefix):
                if len(inner) < 3:
                    inner.append(p)
        res.append(inner)
    return res

