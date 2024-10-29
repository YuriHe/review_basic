class TrieNode:
    # create TriNode class having character, isEnd, children[] members. children[] store TriNodes(letter) which track next node
    def __init__(self, ch=None):
        self.ch = ch
        self.isEnd = False
        self.children = [None] * 26 # only lowercase

class Trie:
    """
    Dictionary Tree/Trie Tree
    """
    def __init__(self):
        # create Root note
        self.root = TrieNode(ch=None)
        
    def insert(self, word: str) -> None: # O(len(w))
        # build trie tree
        # define cur to track node
        cur = self.root
        for c in word:
            if not cur.children[ord(c) - ord('a')]:
                # if None then create TrieNode
                cur.children[ord(c) - ord('a')] = TrieNode(c)
            # track next node with lettter
            cur = cur.children[ord(c) - ord('a')]
        # finsih iterate word
        cur.isEnd = True

    def search(self, word: str) -> bool: # O(len(w))
        cur = self.root
        for c in word:
            if not cur.children[ord(c)-ord('a')]:
                # this Trienode not exist
                return False
            else:
                cur = cur.children[ord(c)-ord('a')]
        return cur.isEnd 
        
    def startsWith(self, prefix: str) -> bool: # O(len(p))
        cur = self.root
        for c in prefix:
            if not cur.children[ord(c)-ord('a')]:
                return False
            else:
                cur = cur.children[ord(c)-ord('a')]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)