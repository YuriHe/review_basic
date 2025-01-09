"""
208. Implement Trie
"""
class Node:
    def __init__(self, char = None):
        self.val = char
        self.child = [None] * 26 # store node
        self.end = False

class Trie:

    def __init__(self):
        # create tree node
        self.root = Node()
        
    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            idx = ord(c) - ord('a')
            if cur.child[idx] is None:
                cur.child[idx] = Node(c)
            cur = cur.child[idx]
        cur.end = True
    
    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            idx = ord(c) - ord('a')
            if cur.child[idx] is None:
                return False
            cur = cur.child[idx]
        return cur.end
        
    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            idx = ord(c) - ord('a')
            if cur.child[idx] is None:
                return False
            cur = cur.child[idx]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


"""
211. Design Add and Search Words Data Structure
"""
class Node:
    def __init__(self, char = None):
        self.val = char
        self.child = {} # char: Node; use {} if all characters, use[None]*26 if only lowercaser letters
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = Node()
        
    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.child:
                cur.child[c] = Node(c)
            cur = cur.child[c]
        cur.end = True
            
    def search(self, word: str) -> bool:
        cur = self.root

        # dfs go through whole woord
        def dfs(idx, cur):
            # handle node is None
            if cur is None:
                return False
            # reach end of word
            if idx == len(word):
                return cur.end

            if word[idx] == '.':
                # recursion call when iterate each key in child dict
                for k in cur.child:
                    if dfs(idx+1, cur.child[k]): # find one path meet
                        return True
                # try all paths, fail to find word
                return False
            else:
                if word[idx] not in cur.child:
                    return False
                else:
                    # keep search next char in word from word[idx]'s all children
                    return dfs(idx+1, cur.child[word[idx]])

        return dfs(0, cur)

# Best 211       
from functools import cache
class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            idx = ord(c) - ord('a')
            if not cur.children[idx]:
                cur.children[idx] = TrieNode()
            cur = cur.children[idx]
        cur.isEnd = True

    def search(self, word: str) -> bool:
        @cache
        def dfs(node, idx):
            # Null check
            if not node: return False
            # base case
            if idx == len(word):
                return node.isEnd

            if word[idx] == ".":
                for child in node.children:
                    if dfs(child, idx+1):
                        return True
                return False
            else:
                # check if this exist
                index = ord(word[idx]) - ord('a')
                return dfs(node.children[index], idx+1)
        return dfs(self.root, 0)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)